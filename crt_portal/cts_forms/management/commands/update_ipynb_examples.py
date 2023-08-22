from typing import Dict, Tuple, TypeVar, Generic, Callable
from datetime import datetime
import json
import os
import sys
import traceback
from types import SimpleNamespace
import uuid

from analytics.models import AnalyticsFile

from django.conf import settings
from django.core.management.base import BaseCommand
import nbconvert
import nbformat
import pytz

notebook_dir = os.path.join(settings.BASE_DIR, '..', 'jupyterhub')


def _simplify_path(path) -> str:
    return path.replace(notebook_dir, '')


def _should_keep(path: str) -> bool:
    if '.ipynb_checkpoints' in path:
        return False
    if 'node_modules/' in path:
        return False
    if '__pycache__' in path:
        return False
    if 'jupyterhub.sqlite' in path:
        return False
    return True


def _build_error_notebook(error: Exception):
    return json.dumps({
        "cells": [
            {
                "cell_type": "markdown",
                "id": str(uuid.uuid4()),
                "metadata": {},
                "source": [
                    "# Something went wrong on import\n",
                    "\n",
                    "We were unable to import this notebook:"
                    "\n",
                    "```",
                    *traceback.format_exception(error),
                    "```",
                ]
            },
        ],
        "metadata": {
            "kernelspec": {
                "display_name": "Python 3 (ipykernel)",
                "language": "python",
                "name": "python3"
            },
            "language_info": {
                "codemirror_mode": {
                    "name": "ipython",
                    "version": 3
                },
                "file_extension": ".py",
                "mimetype": "text/x-python",
                "name": "python",
                "nbconvert_exporter": "python",
                "pygments_lexer": "ipython3",
                "version": '.'.join(str(i) for i in sys.version_info[:3])
            }
        },
        "nbformat": 4,
        "nbformat_minor": 5
    })


DiffKey = TypeVar('DiffKey')
DiffValue = TypeVar('DiffValue')


class DictDiff(SimpleNamespace, Generic[DiffKey, DiffValue]):
    removed: Dict[DiffKey, DiffValue]
    added: Dict[DiffKey, DiffValue]
    changed: Dict[DiffKey, Tuple[DiffValue, DiffValue]]


def _diff_dicts(before: Dict[DiffKey, DiffValue],
                after: Dict[DiffKey, DiffValue],
                is_same: Callable[[DiffValue, DiffValue], bool]) -> DictDiff:
    removed = {
        key: before[key]
        for key
        in before.keys() - after.keys()
    }

    added = {
        key: after[key]
        for key
        in after.keys() - before.keys()
    }

    changed = {
        key: (before[key], after[key])
        for key
        in after.keys() & before.keys()
        if not is_same(before[key], after[key])
    }

    return DictDiff(removed=removed, added=added, changed=changed)


class Command(BaseCommand):  # pragma: no cover
    help = 'Adds new response templates or updates existing ones'

    def _build_notebook(self, notebook_path: str) -> dict:
        local_tz = pytz.timezone('US/Eastern')
        simple_path = _simplify_path(notebook_path)
        return {
            'name': os.path.basename(simple_path).strip('/'),
            'path': simple_path.strip('/'),
            'type': 'notebook',
            'format': 'json',
            'mimetype': 'application/json',
            'created': datetime.fromtimestamp(os.path.getctime(notebook_path), tz=local_tz),
            'last_modified': datetime.fromtimestamp(os.path.getmtime(notebook_path), tz=local_tz),
            'from_command': True
        }

    def _load_notebook(self, notebook_path: str) -> AnalyticsFile:
        with open(notebook_path, 'r') as f:
            node = nbformat.read(f, as_version=nbformat.NO_CONVERT)

        # We don't want to show output from runs in other environments.
        nbconvert.preprocessors.ClearOutputPreprocessor().preprocess(node, {})
        notebook_content = json.dumps(node)
        return AnalyticsFile(
            content=notebook_content,
            **self._build_notebook(notebook_path),
        )

    def _safe_load_notebook(self, notebook_path: str) -> AnalyticsFile:
        try:
            return self._load_notebook(notebook_path)
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error loading notebook {notebook_path}: {e}'))
            return AnalyticsFile(
                content=_build_error_notebook(e),
                **self._build_notebook(notebook_path),
            )

    def _safe_load_directory(self, directory_path: str) -> AnalyticsFile:
        return AnalyticsFile(
            type='directory',
            format='json',
            **self._build_filesystem_object(directory_path),
        )

    def _safe_load_file(self, file_path: str) -> AnalyticsFile:
        try:
            with open(file_path, 'r') as f:
                content = f.read()
        except Exception as e:
            content = str(e)

        return AnalyticsFile(
            content=content,
            type='file',
            **self._build_filesystem_object(file_path),
        )

    def _build_filesystem_object(self, directory_path: str) -> dict:
        local_tz = pytz.timezone('US/Eastern')
        simple_path = _simplify_path(directory_path)
        return {
            'name': os.path.basename(simple_path).strip('/'),
            'path': simple_path.strip('/'),
            'created': datetime.fromtimestamp(os.path.getctime(directory_path), tz=local_tz),
            'last_modified': datetime.fromtimestamp(os.path.getmtime(directory_path), tz=local_tz),
            'from_command': True
        }

    def _gather_files_from_code(self):
        files = []
        for (dirpath, dirnames, filenames) in os.walk(notebook_dir):
            for filename in filenames:
                if not filename.endswith('.ipynb'):
                    continue
                notebook_path = os.path.join(dirpath, filename)
                if not _should_keep(notebook_path):
                    continue
                files.append(self._safe_load_notebook(notebook_path))
            for dirname in dirnames:
                directory_path = os.path.join(dirpath, dirname)
                if not _should_keep(directory_path):
                    continue
                files.append(self._safe_load_directory(directory_path))
            for filename in filenames:
                if filename.endswith('.ipynb'):
                    continue
                file_path = os.path.join(dirpath, filename)
                if not _should_keep(file_path):
                    continue
                files.append(self._safe_load_file(file_path))

        files.append(self._safe_load_directory('/'))
        return files

    def _preview_file_changes(self, diff: DictDiff):
        count = len(diff.added) + len(diff.changed) + len(diff.removed)
        self.stdout.write(self.style.SUCCESS('\n'.join([
            f'Updating {count} Jupyter objects from filesystem:',
            *[f'  + (added) {added} ' for added in diff.added],
            *[f'  ! (changed) {changed}' for changed in diff.changed],
            *[f'  - (removed) {removed}' for removed in diff.removed],
        ])))

    def _update_files(self, diff: DictDiff) -> int:
        to_delete = [
            *diff.removed.values(),
            *[before for before, _ in diff.changed.values()],
        ]
        to_create = [
            *diff.added.values(),
            *[after for _, after in diff.changed.values()],
        ]
        for file in to_delete:
            file.delete()
        AnalyticsFile.objects.bulk_create(to_create)
        return len(to_create)

    def handle(self, *args, **options):
        del args, options  # Unused

        code_files = {
            (file.name, file.path): file
            for file
            in self._gather_files_from_code()
        }
        database_files = {
            (file.name, file.path): file
            for file
            in AnalyticsFile.objects.filter(from_command=True)
        }

        diff = _diff_dicts(
            database_files,
            code_files,
            lambda before, after: before.has_same_source_as(after)
        )

        self._preview_file_changes(diff)

        total_created = self._update_files(diff)
        self.stdout.write(self.style.SUCCESS(f'Loaded {total_created} Jupyter objects from filesystem'))

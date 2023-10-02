# Generated by Django 4.2.3 on 2023-09-06 14:23

from django.db import migrations
from features.models import AddFeatureMigration


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0009_disposition'),
    ]

    operations = [
        AddFeatureMigration(
            'email_responses_card',
            True,
            description='Show the email responses card on the report detail page.'
        ),
    ]

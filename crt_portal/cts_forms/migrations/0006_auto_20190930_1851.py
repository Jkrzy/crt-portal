# Generated by Django 2.2.4 on 2019-09-30 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0005_auto_20190925_1542'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='violation_summary',
            field=models.TextField(max_length=7000),
        ),
    ]

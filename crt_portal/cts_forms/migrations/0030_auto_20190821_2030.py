# Generated by Django 2.2.4 on 2019-08-21 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0029_auto_20190821_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='relationship',
            field=models.CharField(choices=[('parent_guardian', 'Im a parent or guardian of the person affected'), ('professional', 'Im providing professional assistance'), ('witness to the situation', 'Im a witness to the situation')], default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='who_reporting_for',
            field=models.CharField(choices=[('myself', "I'm reporting for myself"), ('another', "I'm reporting on behalf of another person"), ('undisclosed', 'I prefer not to disclose')], default=None, max_length=100),
        ),
    ]
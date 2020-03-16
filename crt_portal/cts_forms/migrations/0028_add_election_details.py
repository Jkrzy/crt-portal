# Generated by Django 2.2.4 on 2019-12-16 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0025_make_hatecrimes_question_optional'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='election_details',
            field=models.CharField(blank=True, choices=[('federal', 'Federal- presidential, or congressional'), ('state_local', 'State or local- Governor, state legislation, city position (mayor, council, local board)'), ('both', 'Both Federal & State/local'), ('unknown', 'I don’t know')], max_length=225, null=True),
        ),
    ]

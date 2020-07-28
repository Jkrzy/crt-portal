# Generated by Django 2.2.12 on 2020-06-16 17:33

from django.db import migrations


def tweak_templates(apps, schema_editor):
    ResponseTemplate = apps.get_model('cts_forms', 'ResponseTemplate')
    nonactionable = ResponseTemplate.objects.get(title='Non-Actionable')
    # adjust addressee and indentation
    nonactionable.template = """{{ addressee }},

You contacted the Department of Justice on {{ date_of_intake }}. After careful review of what you submitted, we have decided not to take any further action on your complaint.

What we did:

Team members from the Civil Rights Division reviewed the information you submitted.  Based on this information, our team determined that the federal civil rights laws we enforce do not cover the situation you described.  Therefore, we cannot take further action.

Your record number is {{ record_locator }}.

What you can do:

Your issue may be covered by other federal, state, or local laws that we do not have the authority to enforce. We are not determining that your report lacks merit.

Your state bar association or local legal aid office may be able to help with your issue even though the Department of Justice cannot.

    To find a local office:

    American Bar Association
    www.findlegalhelp.org
    (800) 285-2221

    Legal Service Corporation (or Legal Aid Offices)
    www.lsc.gov/find-legal-aid
    (202) 295-1500

Thank you for taking the time to contact the Department of Justice about your concerns. We regret that we are not able to provide more help on this matter.

Sincerely,

U.S. Department of Justice
Civil Rights Division
"""
    nonactionable.save()

    nocapacity = ResponseTemplate.objects.get(title='No capacity')
    # adjust addressee and indentation
    nocapacity.template = """{{ addressee }},

You contacted the Department of Justice on {{ date_of_intake }}. After careful review of what you submitted, we have decided not to take any further action on your complaint.

What we did:

Team members from the Civil Rights Division reviewed the information you submitted.  Based on our review, we have decided not to take any further action on your complaint.  We receive several thousand reports of civil rights violations each year.  We unfortunately do not have the resources to take direct action for every report.

Your record number was {{ record_locator }}.

What you can do:

We are not determining that your report lacks merit. Your issue may still be actionable by others - your state bar association or local legal aid office may be able to help.

    To find a local office:

    American Bar Association
    www.findlegalhelp.org
    (800) 285-2221

    Legal Service Corporation (or Legal Aid Offices)
    www.lsc.gov/find-legal-aid
    (202) 295-1500

How you have helped:

While we don’t have the capacity to take on each individual report, your report can help us find issues affecting multiple people or communities. It also helps us understand emerging trends and topics.

Thank you for taking the time to contact the Department of Justice about your concerns.  We regret we are not able to provide more help on this matter.

Sincerely,

U.S. Department of Justice
Civil Rights Division
"""
    nocapacity.save()


def untweak_templates(apps, schema_editor):
    # don't prevent unmigrations. if we want to undo these tweaks,
    # best to unmigrate to 0074 and then migrate up to 0077.
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('cts_forms', '0077_report_add_date_closed'),
    ]

    operations = [
        migrations.RunPython(tweak_templates, untweak_templates),
    ]

import logging
from datetime import datetime

from django.conf import settings
from django.core.mail import send_mail
from tms.models import TMSEmail

logger = logging.getLogger(__name__)


def remove_disallowed_recipients(recipient_list):
    """
    If we've limited the recipients, modify the `to` attribute of our email_message
    """
    # If the list of restrictions is empty, allow all
    restricted_to = settings.RESTRICT_EMAIL_RECIPIENTS_TO
    if restricted_to:
        recipient_list = [
            to_address
            for to_address in recipient_list
            if to_address in restricted_to
        ]
    return recipient_list


def crt_send_mail(report, template):
    """
    Given a report and a template, use django's builtin `send_mail` to generate and send
    an outbound email

    Returns a reference to the delivered TMSAPI request
    """
    subject = template.render_subject(report)
    message = template.render_body(report)

    recipient_list = remove_disallowed_recipients([report.contact_email])
    if not recipient_list:
        logger.info(f'{report.contact_email} not in allowed domains, not attempting to deliver email response template #{template.id} to report: {report.id}')
        return None
    send_results = send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, recipient_list, fail_silently=False)
    logger.info(f'Sent email response template #{template.id} to report: {report.id}')
    if settings.EMAIL_BACKEND == 'tms.backend.TMSEmailBackend':
        response = send_results[0]
        TMSEmail(tms_id=response['id'],
                 recipient=report.contact_email,
                 subject=subject,
                 body=message,
                 report=report,
                 created_at=datetime.strptime(response['created_at'], '%Y-%m-%dT%H:%M:%S%z'),
                 status=response['status']
                 ).save()
    return send_results

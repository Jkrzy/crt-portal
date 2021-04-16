
from django.test import SimpleTestCase, override_settings
from cts_forms.mail import remove_disallowed_recipients


class CrtSendMailTests(SimpleTestCase):

    @override_settings(RESTRICT_EMAIL_RECIPIENT_DOMAINS_TO=['test.com'])
    def test_remove_disallowed_recipients(self):
        """
        Targets for email messages are removed if the domain is not found in
        the recipients list
        """
        recipients = ['to1@example.com', 'to2@test.com']
        self.assertEquals(remove_disallowed_recipients(recipients), ['to2@test.com'])

        recipients = ['to1@example.com']
        self.assertEquals(remove_disallowed_recipients(recipients), [])

    @override_settings(RESTRICT_EMAIL_RECIPIENT_DOMAINS_TO=[])
    def test_dont_remove_disallowed_recipients_if_none(self):
        """
        Targets for email messages not modified if no restrictions
        """
        recipients = ['to1@example.com', 'to2@test.com']
        self.assertEquals(remove_disallowed_recipients(recipients), recipients)

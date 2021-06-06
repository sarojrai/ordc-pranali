import os

from django.core import mail
from django.template.loader import get_template, render_to_string
from django.template import Context

from ordc.settings import EMAIL_HOST_USER, BASE_DIR


class EmailService:

    def invitation_email(self, token, email):
        # TODO use ini file to load base url and App Name of UI
        with mail.get_connection() as connection:
            subject = "You have been invited to {app_name}".format(
                app_name='Reverse Auction')
            invitation_url = "http://{base_url}/invitation_complete/?invitation_token={token}".format(
                base_url='localhost:4040', token=token)
            data = {'email': email, 'invitation_url': invitation_url}
            html_content = render_to_string('email/invitation.html', data)
            print(html_content)
            msg = mail.EmailMessage(
                subject, html_content, EMAIL_HOST_USER, [email], connection=connection)
            msg.attach_alternative(html_content, "text/html")
            msg.send()

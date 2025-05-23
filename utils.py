from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from datetime import datetime
from django.conf import settings


def send_notification_email(to_email, heading, message, subject=""):
    context = {
        "subject": subject,
        "heading": heading,
        "message": message,
        "year": datetime.now().year
    }

    html_content = render_to_string("emails/notification_email.html", context)
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives(
        subject=subject,
        body=text_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=to_email if isinstance(to_email, list) else [to_email]
    )
    email.attach_alternative(html_content, "text/html")
    email.send()

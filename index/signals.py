from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings

def send_subscribe_mail(email, **kwargs):
    subject= 'AMD Telecom'
    html = render_to_string('subscribe.html')
    send_mail(
        subject=subject,
        message='',
        from_email=settings.EMAIL_HOST_USER, 
        recipient_list=[email],
        html_message=html,
        )
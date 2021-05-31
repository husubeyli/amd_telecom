from django.db.models.signals import post_save
from django.conf import  settings
from django.dispatch import receiver
from django.utils.timezone import now
from django.core.mail import send_mail

from .models import Contact


@receiver(post_save, sender=Contact)
def create_contact(sender, instance, **kwargs):
    first_name = instance.first_name
    last_name = instance.last_name
    phone_number = instance.phone_number
    email = instance.email
    message = instance.message

    subject = 'Contact'
    data = f''' 
        Ad: {first_name}
        Soyad: {last_name}
        Elaqe nömrəsi: {phone_number}
        Elektron poçt ünvanı: {email}
        Mesaj: {message}
    '''
    send_mail(subject, data, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER,])

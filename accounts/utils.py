from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse

def send_verification_email(email):
    verification_url = settings.SITE_URL + reverse('email-verify')
    send_mail(
        'Verify your account',
        f'Please click on the following link to verify your account: {verification_url}',
        settings.DEFAULT_FROM_EMAIL,
        [email],
        fail_silently=False,
    )
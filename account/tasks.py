from celery import shared_task
from rest_framework.authtoken.models import Token
from django.core.mail import send_mail
from django.utils.html import strip_tags
from .models import CustomUser
from decouple import config

@shared_task
def send_confirmation_email_task(user_id):
    user = CustomUser.objects.get(pk=user_id)
    token, created = Token.objects.get_or_create(user=user)
    subject = 'Confirm your email address'
    message = (
        f"Привет {user.email},\n\n"
        f"Пожалуйста, подтвердите свой адрес электронной почты, нажав на ссылку ниже:\n"
        f"http://{config('DOMEN')}/confirm-email/?token={token.key}"
    )


    from_email = 'bagishan040401@yandex.ru'
    to_email = user.email

    send_mail(subject, message, from_email, [to_email])




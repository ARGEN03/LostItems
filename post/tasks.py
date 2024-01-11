from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from .models import Post

@shared_task
def send_comment_notification(post_id, comment_text):
    post = Post.objects.get(pk=post_id)
    owner_email = post.owner.email

    subject = 'Уведомление о новом комментарии'
    message = f'Привет {post.owner.username},\n\nКто-то добавил комментарий к вашему посту:\n\n"{comment_text}"'
    from_email = 'bagishan040401@yandex.ru'  # Обновите свой адрес электронной почты
    recipient_list = [owner_email]

    send_mail(subject, message, from_email, recipient_list)
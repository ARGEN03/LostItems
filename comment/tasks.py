from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from post.models import Post
from .models import Comment



@shared_task
def send_comment_notification(comment_id):
    comment = Comment.objects.get(pk=comment_id)
    post = comment.post
    owner_email = post.owner.email

    subject = 'Уведомление о новом комментарии'
    message = f'Привет {post.owner.username},\n\nКто-то добавил комментарий к вашему посту:\n\n"{comment.content}"'
    from_email = 'bagishan040401@yandex.ru'
    recipient_list = [owner_email]

    send_mail(subject, message, from_email, recipient_list)
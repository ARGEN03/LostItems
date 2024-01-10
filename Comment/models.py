from django.db import models
from post.models import Post
from account.models import CustomUser

# Create your models here.


class Comment(models.Model):
    content = models.TextField()
    owner = models.ForeignKey(
        CustomUser,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
    created_at = models.DateField(auto_now_add = True)
    post = models.ForeignKey(
        Post,
        on_delete = models.CASCADE,
        related_name = 'comments'
    )
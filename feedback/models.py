from django.db import models
from post.models import Post
from account.models import CustomUser

# Create your models here.
class Feedback(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='feedbacks')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} - {self.post.title}'
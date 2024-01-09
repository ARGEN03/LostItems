from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    # category 
    # image
    image = models.ImageField(upload_to='images/', null=True)
    # owner 
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
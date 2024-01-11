from django.db import models
from Category.models import Category
from account.models import CustomUser

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    desc = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE, related_name='posts', default='Found')
    image = models.ImageField(upload_to='images/', null=True)
    owner = models.ForeignKey(CustomUser,related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
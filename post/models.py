from django.db import models
from account.models import CustomUser
from category.models import Category

# Create your models here.
class Post(models.Model):
    FOUND = 'Found'
    LOST = 'Lost'

    CHOICES = (
        (FOUND, 'Найден'),
        (LOST, 'Потерян')
    )

    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=CHOICES)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(upload_to='images/', null=True)
    owner = models.ForeignKey(CustomUser,related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.title
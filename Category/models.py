from django.db import models

# Create your models here.


class Category(models.Model):
    CHOICE = (
        ('Found','Нашел'),
        ('Lost','Потерял')
    )
    

    choice = models.CharField(max_length = 150, choices=CHOICE)
    parent = models.ForeignKey(
        'self',
        on_delete = models.SET_NULL,
        null=True, blank=True,
        related_name = 'children'       
        )
    
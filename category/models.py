from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(
        'self',
        on_delete = models.SET_NULL,
        null=True, blank=True,
        related_name = 'children'       
        )

    def __str__(self) -> str:
        return self.name
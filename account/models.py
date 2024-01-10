from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150, null=True, blank=True)
    whatsapp = models.CharField(max_length=150, null=True, blank=True)
    # password = models.CharField(max_length=150)
    # password_confirmation = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone_number']

    objects = CustomUserManager() 


    def __str__(self):
        return self.email


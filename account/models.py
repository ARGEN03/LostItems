# from django.db import models
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.hashers import make_password
# # Create your models here.

# class Account(models.Model):
#     username = models.CharField(max_length=150)
#     email = models.EmailField(max_length=150)
#     password = models.CharField()
#     password_confirmation = models.CharField()
#     phone_number = models.CharField()
#     telegram = models.CharField(max_length=150, null=True)
#     whatsapp = models.CharField(null=True)
#     # last_login = models.DateTimeField(_("last login"), null=True, blank=True)

#     def set_password(self, raw_password):
#         self.password = make_password(raw_password)
#         self._password = raw_password


from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager


class CustomUser(AbstractBaseUser):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=150)
    telegram = models.CharField(max_length=150, null=True, blank=True)
    whatsapp = models.CharField(max_length=150, null=True, blank=True)
    password = models.CharField(max_length=150)
    password_confirmation = models.CharField(max_length=150)



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager() 


    def __str__(self):
        return self.email


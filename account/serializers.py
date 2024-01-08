from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True, min_length=8, write_only=True)
    password_confirmation = serializers.CharField(required=True, min_length=8, write_only=True)
    phone_number = serializers.CharField(required=True, min_length=9)
    telegram = serializers.CharField(max_length=150)
    whatsapp = serializers.CharField(min_length=9)

    class Meta:
        model=User
        fields=['username', 'email', 'password', 'password_confirmation', 'phone_number', 'telegram', 'whatsapp']


    def validate(self, attrs):
        password_conf = attrs.pop('password_confirmation')
        if password_conf != attrs['password']:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        if not attrs['first_name'].istitle():
            raise serializers.ValidationError(
                'Имя должно начинатся с заглавной буквы'
            )
        return attrs
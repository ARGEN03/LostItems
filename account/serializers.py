# from .models import CustomUser


# class RegisterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model=Account
#         fields='__all__'


#     def validate(self, attrs):
#         password_conf = attrs.pop('password_confirmation')
#         if password_conf != attrs['password']:
#             raise serializers.ValidationError(
#                 'Пароли не совпадают'
#             )
#         return attrs
    
#     def create(self, validated_data):
#         user = Account.objects.create(**validated_data)
#         user.set_password(validated_data['password'])
#         user.save()
#         return user
    
# class LoginSerializer(serializers.Serializer):
#     email = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         email = data.get('email')
#         print(email)
#         password = data.get('password')
#         print(password)
#         request = self.context.get('request')
#         print(request)
#         if email and password:
#             user = authenticate(
#                 request=request,
#                 email=email,
#                 password=password,
#                 # backends='django.contrib.auth.backends.EmailBackend'
#             )
#             print(user)
#             if not user:
#                 raise serializers.ValidationError(
#                     'Не правильный пароль или почта'
#                 )
#         else:
#             raise serializers.ValidationError(
#                 'Вы забыли запонить email или password'
#             )
#         data['user'] = user
#         return data
    
#     def validate_email(self, email):
#         if not Account.objects.filter(email=email).exists():
#             raise serializers.ValidationError(
#                 'user not found'
#             )
#         return email
    
# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Account
#         fields = '__all__'
from django.contrib.auth.models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import CustomUser


class RegisterSerializer(serializers.ModelSerializer):
    # phone_number = serializers.CharField(min_length=9, required=True)
    # password = serializers.CharField(required=True, min_length=8, write_only=True)
    # password_confirmation = serializers.CharField(required=True, min_length=8, write_only=True)


    class Meta:
        model=CustomUser
        fields='__all__'

    
    def validate(self, attrs):
        password_conf = attrs.pop('password_confirmation')
        if password_conf != attrs['password']:
            raise serializers.ValidationError(
                'Пароли не совпадают'
            )
        return attrs
    
    def create(self, validated_data):
        user = CustomUser.objects.create(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        print(email)
        password = data.get('password')
        print(password)
        request = self.context.get('request')
        if email and password:
            user = authenticate(
                email=email,
                password=password,
                request=request
            )
            print(user)
            if not user:
                raise serializers.ValidationError(
                    'Не правильный пароль или юзернейм'
                )
        else:
            raise serializers.ValidationError(
                'Вы забыли запонить email или password'
            )
        data['user'] = user
        return data
    
    def validate_email(self, email):
        if not CustomUser.objects.filter(email=email).exists():
            raise serializers.ValidationError(
                'email not found'
            )
        return email
    

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = User
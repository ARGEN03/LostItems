from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status
from rest_framework import generics
from rest_framework import permissions
from .tasks import send_confirmation_email_task

from .serializers import RegisterSerializer, LoginSerializer, UserDetailSerializer
from .serializers import UserSerializer
from .models import CustomUser


class UserRegistration(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
    
        send_confirmation_email_task.delay(user.id)

        return Response('Account is created. Confirmation email will be sent.', status=status.HTTP_201_CREATED)
    

class UserDetail(APIView):
    def get_object(self, user_id):
        try:
            return CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise Response("User not found", status=status.HTTP_404_NOT_FOUND)

    def patch(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('Account is updated', status=status.HTTP_200_OK)

    def delete(self, request, user_id):
        user = self.get_object(user_id)
        user.delete()
        return Response('Account is deleted', status=status.HTTP_204_NO_CONTENT)

    
class LoginView(ObtainAuthToken):
    serializer_class = LoginSerializer
    
    def post(self, request):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, _ = Token.objects.get_or_create(user=user)

        response_data = {
            'token':token.key,
            'username':user.username,
            'id':user.id
        }
        return Response(response_data)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response('успешно вышли с аккаунта')





class UserListAPIView(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

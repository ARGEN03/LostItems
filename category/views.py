
from rest_framework.viewsets import ModelViewSet

from category import permissions
from .models import Category
from .serializers import CategorySerializer
from rest_framework import permissions
from .permissions import IsStaff
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE','POST']:
            return [permissions.IsAuthenticated(), IsStaff()]
        return [permissions.AllowAny()]
    
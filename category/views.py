from rest_framework.viewsets import ModelViewSet
from category import permissions
from historysearch.models import SearchHistory
from historysearch.serializers import SearchHistorySerializer
from .models import Category
from .serializers import CategorySerializer
from rest_framework import permissions
from .permissions import IsStaff
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
# Create your views here.

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE','POST']:
            return [permissions.IsAuthenticated(), IsStaff() ]
        return [permissions.AllowAny()]
    
    def list(self, request, *args, **kwargs):
        query = self.request.query_params.get('search', '')
        if query:
            SearchHistory.objects.create(user=self.request.user, query=query)

        return super().list(request, *args, **kwargs)
        
class SearchHistoryView(generics.ListAPIView):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer

    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
    
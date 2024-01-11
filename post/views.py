from rest_framework.viewsets import ModelViewSet
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerAndAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination


# Create your views here.
class StandartResultPagination(PageNumberPagination):
    page_size = 5
    page_query_param= 'page'


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerAndAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['status']
    ordering_fiedls = ['status', 'created_at', 'title']
    pagination_class = StandartResultPagination
     



    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
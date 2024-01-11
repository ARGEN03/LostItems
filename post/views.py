from rest_framework.viewsets import ModelViewSet
from drf_yasg.utils import swagger_auto_schema
from comment.serializers import CommentSerializer
from .models import Post
from .serializers import PostSerializer
from .permissions import IsOwnerAndAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response



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
     
    @swagger_auto_schema(method='POST', request_body=CommentSerializer, operation_description='add comment for post')
    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post, owner=request.user)
        return Response('успешно добавлено', 201)


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
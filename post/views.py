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
from historysearch.models import SearchHistory
from historysearch.serializers import SearchHistorySerializer
from rest_framework import generics
import logging


# logger = logging.getLogger('main')
# Create your views here.
class StandartResultPagination(PageNumberPagination):
    page_size = 5
    page_query_param= 'page'


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [IsOwnerAndAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['title', 'description']
    filterset_fields = ['status']
    ordering_fields = ['status', 'created_at', 'title']
    pagination_class = StandartResultPagination

    # def list(self, request, *args, **kwargs):
    #     print('DEBUG: Post List View Called')
    #     logger.error('Post List View Called')
    #     return super().list(request, *args, **kwargs)

    # def create(self, request, *args, **kwargs):
    #     logger.error('Post Create View Called')
    #     return super().create(request, *args, **kwargs)

    # def retrieve(self, request, *args, **kwargs):
    #     logger.error('Post Retrieve View Called')
    #     return super().retrieve(request, *args, **kwargs)

    # def update(self, request, *args, **kwargs):
    #     logger.error('Post Update View Called')
    #     return super().update(request, *args, **kwargs)

    # def partial_update(self, request, *args, **kwargs):
    #     logger.error('Post Partial Update View Called')
    #     return super().partial_update(request, *args, **kwargs)

    # def destroy(self, request, *args, **kwargs):
    #     logger.error('Post Destroy View Called')
    #     return super().destroy(request, *args, **kwargs)
     
    @swagger_auto_schema(method='POST', request_body=CommentSerializer, operation_description='add comment for post')
    @action(detail=True, methods=['POST'])
    def comment(self, request, pk=None):
        post = self.get_object()
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(post=post, owner=request.user)
        return Response('успешно добавлено', 201)


    def list(self, request, *args, **kwargs):
        # Сохраняем результаты поиска в истории
        query = self.request.query_params.get('search', '')
        if query:
            SearchHistory.objects.create(user=self.request.user, query=query)

        return super().list(request, *args, **kwargs)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
        
class SearchHistoryView(generics.ListAPIView):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer

    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from .models import Comment
from .serializers import CommentSerializer
from .permissions import IsOwnerAndAuthenticatedOrReadOnly
from .tasks import send_comment_notification

# # Create your views here.
# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsOwnerAndAuthenticatedOrReadOnly]

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)



# from .models import Comment
# from .serializers import CommentSerializer

# class CommentViewSet(ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated]

#     def perform_create(self, serializer):
#         comment = serializer.save()
#         post_id = comment.post.id
#         comment_text = comment.text

#         # Вызовите задачу Celery для отправки электронного письма асинхронно
#         send_comment_notification.delay(post_id, comment_text)




class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerAndAuthenticatedOrReadOnly, IsAuthenticated]

    def perform_create(self, serializer):
        comment = serializer.save(owner=self.request.user)

        # Вызовите задачу Celery для отправки электронного письма асинхронно
        send_comment_notification.delay(comment.id)
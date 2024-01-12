from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Comment, Like
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

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        comment = self.get_object()
        user = request.user
        like, created = Like.objects.get_or_create(user=user, comment=comment)

        if not created:
            like.delete()
            liked = False
        else:
            liked = True

        serializer = self.get_serializer(comment)
        return Response({'liked': liked, 'comment': serializer.data})

    def perform_create(self, serializer):

        comment = serializer.save(owner=self.request.user)
        serializer.save(owner=self.request.user)

        send_comment_notification.delay(comment.id)



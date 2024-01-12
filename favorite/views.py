from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Post, Favorite
from .serializers import FavoriteSerializer

class ToggleFavoriteView(generics.CreateAPIView, generics.DestroyAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        post_id = self.kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)
        return get_object_or_404(Favorite, owner=self.request.user, post=post)

    def create(self, request, *args, **kwargs):
        post_id = kwargs['post_id']
        post = get_object_or_404(Post, id=post_id)

        if Favorite.objects.filter(owner=request.user, post=post).exists():
            return Response({'message': 'Post already in favorites.'}, status=status.HTTP_400_BAD_REQUEST)

        Favorite.objects.create(owner=request.user, post=post)
        return Response({'message': 'Post added to favorites successfully.'}, status=status.HTTP_201_CREATED)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Post removed from favorites successfully.'}, status=status.HTTP_200_OK)
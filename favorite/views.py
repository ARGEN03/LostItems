from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Favorite
from post.models import Post

@api_view(['POST', 'DELETE'])
@permission_classes([IsAuthenticated])
def toggle_favorite(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user

    if request.method == 'POST':
        if Favorite.objects.filter(user=user, post=post).exists():
            return Response({'message': 'Post already in favorites.'}, status=400)
        
        favorite = Favorite(user=user, post=post)
        favorite.save()

        return Response({'message': 'Post added to favorites successfully.'}, status=200)
    elif request.method == 'DELETE':
        favorite = get_object_or_404(Favorite, user=user, post=post)
        favorite.delete()

        return Response({'message': 'Post removed from favorites successfully.'}, status=200)
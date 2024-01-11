from rest_framework import serializers
from .models import Comment
from account.models import CustomUser
from post.models import Post

class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())
    
    class Meta:
        model = Comment
        fields = "__all__"

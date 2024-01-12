from rest_framework import serializers
from .models import Favorite
from account.models import CustomUser
from post.models import Post

class FavoriteSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all())

    class Meta:
        model = Favorite
        fields = "__all__"
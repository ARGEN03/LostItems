from .models import Post
from rest_framework import serializers
from Category.models import Category


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Category.objects.all()
    )

    class Meta:
        model = Post
        fields = '__all__'
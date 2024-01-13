from comment.serializers import CommentSerializer
# from feedback.serializers import FeedbackSerializer
from .models import Post
from rest_framework import serializers
from category.models import Category



class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    category = serializers.PrimaryKeyRelatedField(
        required=True, queryset=Category.objects.all()
    )
    comments = serializers.SerializerMethodField(method_name='get_comments')
    # recovery_feedbacks =FeedbackSerializer(many=True, read_only=True)

    def get_comments(self, instance):
        comments = instance.comments.all()
        serializer = CommentSerializer(
            comments, many=True
        )
        return serializer.data


    class Meta:
        model = Post
        fields = '__all__'
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewSet

router = DefaultRouter()
router.register('', PostViewSet, basename='post')

urlpatterns = [
    path('', include(router.urls)),
    path('posts_after_expiry/', PostViewSet.posts_after_expiry, name='post-posts-after-expiry')
]
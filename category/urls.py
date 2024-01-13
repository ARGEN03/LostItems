from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet
from django.views.decorators.cache import cache_page

router = DefaultRouter()
router.register('', CategoryViewSet, basename='category')

urlpatterns = [
    path('',include(router.urls), name='category'),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet


# Create your views here.
router = DefaultRouter()
router.register('', CategoryViewSet, basename='category')

urlpatterns = [
    path('', include(router.urls))
]
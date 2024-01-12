from django.urls import path, include
from .views import FeedbackViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', FeedbackViewSet, basename='feedback')

urlpatterns = [
    path('', include(router.urls))
]
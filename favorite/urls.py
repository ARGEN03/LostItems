from django.urls import path
from .views import toggle_favorite

urlpatterns = [
    path('toggle_favorite/<int:post_id>/', toggle_favorite, name='toggle_favorite'),
]
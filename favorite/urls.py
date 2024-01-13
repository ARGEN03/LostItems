from django.urls import path
from .views import ToggleFavoriteView

urlpatterns = [
    path('favorite/<int:post_id>/', ToggleFavoriteView.as_view(), name='toggle-favorite'),
]
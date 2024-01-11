from django.urls import path
from .views import SearchHistoryListView

urlpatterns = [

    path('search-history/', SearchHistoryListView.as_view(), name='search-history'),
]

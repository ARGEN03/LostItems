from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import SearchHistory
from .serializers import SearchHistorySerializer

class SearchHistoryListView(generics.ListAPIView):
    queryset = SearchHistory.objects.all()
    serializer_class = SearchHistorySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user)
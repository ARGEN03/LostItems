from rest_framework.generics import ListCreateAPIView
from .serializers import SeachHistorySerializer
from rest_framework.permissions import IsAuthenticated
from .models import SearchHistory
# from post.models import 

# Create your views here.
# class YourModelListView(generics.ListAPIView):
#     queryset = YourModel.objects.all()
#     serializer_class = YourModelSerializer
#     filter_backends = [SearchFilter]
#     search_fields = ['field_name1', 'field_name2']

#     def get(self, request, *args, **kwargs):
#         # Сохраняем результаты поиска в истории
#         query = self.request.query_params.get('search', '')
#         if query:
#             SearchHistory.objects.create(user=self.request.user, query=query)

#         return super().get(request, *args, **kwargs)

class SearchHistoryListView(ListCreateAPIView):
    serializer_class = SeachHistorySerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return SearchHistory.objects.filter(user=self.request.user).order_by('-timestamp')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user, query=self.request.query_params.get('search_term'))
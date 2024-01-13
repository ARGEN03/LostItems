from rest_framework.viewsets import ModelViewSet
from .models import Feedback
from .serializers import FeedbackSerializer

# Create your views here.
class FeedbackViewSet(ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
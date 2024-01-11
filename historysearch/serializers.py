from rest_framework import serializers
from .models import SearchHistory


class SeachHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchHistory
        fields = '__all__'
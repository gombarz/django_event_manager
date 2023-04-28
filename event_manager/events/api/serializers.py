from rest_framework import serializers
from events import models

class EventSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Event
        fields = ("id", "name", "date", "author")

class CategorySerializer(serializers.ModelSerializer):

    events = EventSerializer(many=True)
    
    class Meta:
        model = models.Category
        fields = "__all__"
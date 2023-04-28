from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from events import models
from . import serializers

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategorySerializer
    queryset = models.Category.objects.prefetch_related("events", "events__author").all()

    # which kinds of Authentication we allow?
    authentication_classes = (TokenAuthentication,)  # e.g. JWT

    # which permissions are necessary?
    permission_classes = (permissions.IsAuthenticated,)
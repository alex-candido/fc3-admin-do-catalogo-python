from rest_framework import serializers
from core.__seedwork.infra.django_app.serializers import ISO_8601, CollectionSerializer, ResourceSerializer

class CategorySerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField(required=False, allow_blank=True)
    is_active = serializers.BooleanField(required=True)
    created_at = serializers.DateTimeField(read_only=True, format=ISO_8601)
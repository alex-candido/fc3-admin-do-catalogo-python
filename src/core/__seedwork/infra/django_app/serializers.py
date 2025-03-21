from rest_framework import serializers
from core.__seedwork.application.dto import PaginationOutput

class UUIDSerializer(serializers.Serializer): # pylint: disable=abstract-method
    id = serializers.UUIDField()
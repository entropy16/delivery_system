""" Contains the Client serialization classes """
from rest_framework import serializers

from delivery_system.models.client import Client


class ClientSerializer(serializers.ModelSerializer):
    """Serializer for Client model"""
    class Meta:
        model = Client
        fields = ["id", "name", "phone", "email"]

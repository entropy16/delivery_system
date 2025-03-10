""" Contains the Delivery serialization classes """
from rest_framework import serializers
from delivery_system.models.delivery import Delivery


class DeliverySerializer(serializers.ModelSerializer):
    """Serializer for Delivery model"""
    
    client = serializers.SerializerMethodField("get_client")
    cedi = serializers.SerializerMethodField("get_cedi")

    class Meta:
        model = Delivery
        fields = [
            "id", "client", "cedi", "distance", "duration",
            "latitude", "longitude", "created"
        ]
        read_only_fields = ["created"]

    def get_client(self, obj):
        """Returns the client name for the delivery."""
        return obj.client.name

    def get_cedi(self, obj):
        """Returns the cedi name for the delivery."""
        return obj.cedi.name

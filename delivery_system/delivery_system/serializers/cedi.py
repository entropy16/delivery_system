""" Contains the CEDI serialization classes """
from rest_framework import serializers

from delivery_system.models.cedi import CEDI


class CEDISerializer(serializers.ModelSerializer):
    """ CEDI model serializer. """

    class Meta:
        model = CEDI
        fields = ["id", "name", "latitude", "longitude"]

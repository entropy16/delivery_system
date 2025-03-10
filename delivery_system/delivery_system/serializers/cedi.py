""" Contains the CEDI serialization classes """
import pandas as pd

from rest_framework import serializers

from delivery_system.models.cedi import CEDI


class CEDISerializer(serializers.ModelSerializer):
    """ CEDI model serializer. """

    class Meta:
        model = CEDI
        fields = ["id", "name", "latitude", "longitude"]


class CEDIMetricsSerializer(serializers.ModelSerializer):
    """ CEDI model serializer. """

    metrics = serializers.DictField(source="get_metrics")

    class Meta:
        model = CEDI
        fields = ["id", "name", "metrics"]

class CEDIDeliveryTypeSerializer(serializers.ModelSerializer):
    """ CEDI model serializer. """

    deliveries = serializers.SerializerMethodField(source="get_deliveries")

    class Meta:
        model = CEDI
        fields = ["id", "name", "deliveries"]

    def get_deliveries(self, obj):
        """Returns the deliveries for the cedi."""
        if not obj.deliveries.exists():
            return {
                "normal": 0,
                "express": 0
            }

        df = pd.DataFrame(obj.deliveries.values("estimated_duration"))

        avg_duration = df["estimated_duration"].mean()

        return {
            "normal": int(
                df[df["estimated_duration"] >= avg_duration].count()),
            "express": int(df[df["estimated_duration"] < avg_duration].count())
        }

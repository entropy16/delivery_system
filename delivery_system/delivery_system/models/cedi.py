""" Contains the CEDI Django model. """
import pandas as pd

from django.db.models import CharField
from django.db.models import FloatField
from django.db.models import Model
from django.db import models


class CEDI(Model):
    """ Extends class Model.

    Python class representation for CEDI database model
    """
    name = CharField("Nombre", max_length=255)
    latitude = FloatField("Latitud")
    longitude = FloatField("Longitud")

    class Meta:
        """ Meta class for Delivery model. """
        db_table = "cedi"
        ordering = ["id"]
        verbose_name = "Centro de distribución"
        verbose_name_plural = "Centros de distribución"

        constraints = [
            models.UniqueConstraint(
                fields=["latitude", "longitude"],
                name="unique_cedi_coordinates"
            ),
            models.UniqueConstraint(
                fields=["name"],
                name="unique_cedi_name"
            )
        ]

    def __str__(self):
        return f"{self.id}. {self.name}"

    def get_metrics(self):
        """ Returns the CEDI metrics

        Returns:
            dict: CEDI metrics

        """
        deliveries = pd.DataFrame(self.deliveries.values(
            "distance", "estimated_duration"
        ))

        if deliveries.empty:
            return {
                "min_distance": None,
                "max_distance": None,
                "min_duration": None,
                "max_duration": None,
                "avg_speed": None,
                "avg_min_per_km": None
            }

        avg_distance = deliveries["distance"].mean()
        avg_estimated_duration = deliveries["estimated_duration"].mean()

        return {
            "min_distance": deliveries["distance"].min(),
            "max_distance": deliveries["distance"].max(),
            "min_duration": deliveries["estimated_duration"].min(),
            "max_duration": deliveries["estimated_duration"].max(),
            "avg_speed": avg_distance / (avg_estimated_duration / 60),
            "avg_min_per_km": avg_estimated_duration / avg_distance
        }

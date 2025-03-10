""" Contains the CEDI Django model. """
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
        return True

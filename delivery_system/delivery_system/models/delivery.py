""" Contains the Delivery Django model. """
from django_extensions.db.models import TimeStampedModel

from django.contrib.auth.models import User

from django.db.models import CASCADE
from django.db.models import FloatField
from django.db.models import ForeignKey

from delivery_system.helpers.google_routes import get_nearest_cedi
from delivery_system.models.cedi import CEDI
from delivery_system.models.client import Client


class Delivery(TimeStampedModel):
    """ Extends class TimeStampedModel.
    This class add fields created and modified

    Python class representation for Delivery database model
    """

    client = ForeignKey(
        Client, on_delete=CASCADE, related_name="deliveries",
        verbose_name="Cliente")
    cedi = ForeignKey(
        CEDI, on_delete=CASCADE, related_name="deliveries",
        verbose_name="Centro de distribución", null=True, blank=True)
    created_by = ForeignKey(
        User, on_delete=CASCADE, related_name="deliveries",
        verbose_name="Creado por")

    distance = FloatField("Distancia (km)", null=True, blank=True)
    estimated_duration = FloatField(
        "Duración estimada (min)", null=True, blank=True)
    latitude = FloatField("Latitud")
    longitude = FloatField("Longitud")

    class Meta:
        """ Meta class for Delivery model. """
        db_table = "delivery"
        ordering = ["-created"]
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"
        

    def __str__(self):
        return f"{self.id}. {self.client.name} {self.created}"

    def set_cedi(self):
        """ Set the cedi attribute

        Returns:
            bool: True if the cedi was set, False otherwise.

        """
        response = get_nearest_cedi(self)
        if not response:
            return False

        self.cedi = response["cedi"]
        self.distance = response["distance"]
        self.estimated_duration = response["duration"]
        self.save()
        return True

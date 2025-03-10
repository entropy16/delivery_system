""" Contains the Delivery Django model. """
from django_extensions.db.models import TimeStampedModel

from django.db.models import CASCADE
from django.db.models import FloatField
from django.db.models import ForeignKey
from django.db.models import TimeField

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

    distance = FloatField("Distancia", null=True, blank=True)
    duration = TimeField("Duración", null=True, blank=True)
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

""" Contains the Client Django model. """
from django_extensions.db.models import TimeStampedModel

from django.db.models import CharField
from django.db.models import EmailField


class Client(TimeStampedModel):
    """ Extends class TimeStampedModel.
    This class add fields created and modified

    Python class representation for Client database model
    """
    name = CharField("Nombre", max_length=255)
    phone = CharField("Teléfono", max_length=10)
    email = EmailField("Correo", max_length=50)

    class Meta:
        """ Meta class for Client model. """
        db_table = "client"
        ordering = ["id"]
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return f"{self.id}. {self.name} {self.email}"

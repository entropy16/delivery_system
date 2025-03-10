""" Django administrator models """
from django.contrib import admin

from .models import Client
from .models import CEDI


class ClientAdmin(admin.ModelAdmin):
    """ Encapsulate Client fields in django admin """
    search_fields = ["name", "email", "phone"]


class CEDIAdmin(admin.ModelAdmin):
    """ Encapsulate CEDI fields in django admin """
    search_fields = ["name"]


admin.site.register(Client, ClientAdmin)
admin.site.register(CEDI, CEDIAdmin)

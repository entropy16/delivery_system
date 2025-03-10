""" URL configuration for delivery_system project. """
from django.contrib import admin
from django.urls import path

from .views.auth import AuthTokenApi
from .views.cedi import CEDIApi
from .views.cedi import SpecificCEDIApi
from .views.client import ClientApi
from .views.client import SpecificClientApi
from .views.delivery import DeliveryApi
from .views.delivery import SpecificDeliveryApi
from .views.user import PublicUserApi
from .views.user import UserApi
from .views.user import UserDeliveryApi


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth", AuthTokenApi.as_view(), name="auth"),
    path("api/user/register", PublicUserApi.as_view(), name="register_user"),
    path("api/user", UserApi.as_view(), name="user"),
    path("api/user/delivery", UserDeliveryApi.as_view(), name="user_delivery"),
    path("api/cedi", CEDIApi.as_view(), name="cedi"),
    path("api/cedi/<int:cedi_id>", SpecificCEDIApi.as_view(), name="specific_cedi"),
    path("api/client", ClientApi.as_view(), name="client"),
    path("api/client/<int:client_id>", SpecificClientApi.as_view(), name="specific_client"),
    path("api/delivery", DeliveryApi.as_view(), name="delivery"),
    path("api/delivery/<int:delivery_id>", SpecificDeliveryApi.as_view(), name="specific_delivery"),
]

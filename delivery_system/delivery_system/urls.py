""" URL configuration for delivery_system project. """
from django.contrib import admin
from django.urls import path

from .views.auth import AuthTokenApi
from .views.user import UserApi
from .views.user import PublicUserApi


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth", AuthTokenApi.as_view(), name="auth"),
    path("api/user/register", PublicUserApi.as_view(), name="register_user"),
    path("api/user", UserApi.as_view(), name="user")
]

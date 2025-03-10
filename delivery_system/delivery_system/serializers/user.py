""" Contains user serialization classes. """
from rest_framework import serializers

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    """ User model serializer. """
    password = serializers.CharField(
        max_length=128, min_length=8, write_only=True,
        error_messages={
            "min_length": "Password must be at least 8 characters long."
        }
    )
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password"]
        extra_kwargs = {
            "password": {"write_only": True, "min_length": 8}
        }

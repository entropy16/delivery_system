""" Contains the User views definition. """
from cerberus import Validator

from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.models import User
from django.db.models import Q

from delivery_system.helpers.auth import CustomTokenAuthentication

from delivery_system.serializers.user import UserSerializer


class PublicUserApi(APIView):
    """ View for the user's information """

    def post(self, request):
        """ Creates a new user in the platform

        Parameters:
            request: The request object

        Returns:
            dict: The user's information
        
        """
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.create(**serializer.validated_data)
        user.set_password(serializer.validated_data["password"])
        user.save()

        Token.objects.create(user=user)

        return Response({
            "inserted": user.pk
        }, status=status.HTTP_201_CREATED)


class UserApi(APIView):
    """ View for the user's information """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ Returns the user's information

        Parameters:
            request: The request object

        Returns:
            dict: The user's information
        
        """
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request):
        """ Updates the user's information

        Parameters:
            request: The request object

        Returns:
            dict: The user's information

        """
        validator = Validator({
            "username": {
                "required": False, "type": "string", "empty": False
            },
            "email": {
                "required": False, "type": "string", "empty": False
            },
            "password": {
                "required": False, "type": "string", "empty": False
            }
        })
        if not validator.validate(request.data) or not request.data:
            return Response({
                "code": "invalid_body",
                "detailed": "Invalid request body",
                "error": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        if User.objects.filter(
            Q(username=request.data.get("username", None)) |
            Q(email=request.data.get("email", None))
        ).exclude(pk=user.pk).exists():
            return Response({
                "code": "user_already_exists",
                "detailed": (
                    "User with the same username and/or email already exists"
                )
            }, status=status.HTTP_400_BAD_REQUEST)

        if "username" in request.data:
            user.username = request.data["username"]

        if "email" in request.data:
            user.email = request.data["email"]

        if "password" in request.data:
            user.set_password(request.data["password"])

        user.save()

        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        """ Deletes the user's information

        Parameters:
            request: The request object

        Returns:
            dict: The user's information

        """
        user = request.user
        user.delete()

        return Response(status=status.HTTP_200_OK)

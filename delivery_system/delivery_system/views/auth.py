""" Contains the authentication views definition. """
from cerberus import Validator

from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.models import User

from delivery_system.views.user import USER_NOT_FOUND


class AuthTokenApi(APIView):
    """ Custom authentication view that returns the user"s information """

    def post(self, request):
        """ Overridden post method that returns the user's information

        Parameters:
            request: The request object

        Returns:
            dict: The user"s information

        """
        validator = Validator({
            "username": {"required": True, "type": "string", "empty": False},
            "password": {"required": True, "type": "string", "empty": False}
        })
        if not request.data or not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": "Invalid body parameters",
                "error": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.filter(username=request.data["username"]).first()
        if not user:
            return Response(USER_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        if not user.check_password(request.data["password"]):
            return Response({
                "code": "invalid_password",
                "detailed": "Contraseña incorrecta"
            }, status=status.HTTP_400_BAD_REQUEST)

        Token.objects.filter(user=user).delete()

        token = Token.objects.create(user=user)

        return Response({
            "token": token.key,
            "id": user.pk,
            "email": user.email
        })

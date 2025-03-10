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
from delivery_system.helpers.paginator import paginate

from delivery_system.serializers.user import UserSerializer

USER_NOT_FOUND = {
    "code": "user_not_found",
    "detailed": "Usuario no encontrado"
}


class PublicUserApi(APIView):
    """ View for the user's registration """

    def post(self, request):
        """ Creates a new user in the platform

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

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
    """ View for the user's management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """ Returns the user's information

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        users = User.objects.all()

        return Response({
            "count": users.count(),
            "data": paginate(
                UserSerializer(users, many=True).data,
                request.headers
            )
        }, status=status.HTTP_200_OK)

    def put(self, request):
        """ Updates the user's information

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

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
                "detailed": "Cuerpo con estructura inválida",
                "error": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        user = request.user

        if User.objects.filter(
            Q(username=request.data.get("username", None)) |
            Q(email=request.data.get("email", None))
        ).exclude(pk=user.pk).exists():
            return Response({
                "code": "user_already_exists",
                "detailed": "Ya existe un usuario con ese username y/o email"
            }, status=status.HTTP_400_BAD_REQUEST)

        if "password" in request.data:
            user.set_password(request.data.pop("password"))

        User.filter(pk=user.pk).update(**request.data)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request):
        """ Deletes the user's information

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        user = request.user
        user.delete()

        return Response(status=status.HTTP_200_OK)

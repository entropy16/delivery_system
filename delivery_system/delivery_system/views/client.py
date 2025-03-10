""" Contains the Client views definition. """
from cerberus import Validator

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from delivery_system.helpers.auth import CustomTokenAuthentication
from delivery_system.helpers.paginator import paginate

from delivery_system.models.client import Client

from delivery_system.serializers.client import ClientSerializer

EMAIL_REGEX = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
PHONE_REGEX = r"^\d{10}$"

CLIENT_NOT_FOUND = {
    "code": "client_not_found",
    "detailed": "No se ha encontrado el cliente"
}

CLIENT_ALREADY_EXISTS = {
    "code": "client_already_exists",
    "detailed": "Ya existe un cliente con ese correo electrónico"
}


class ClientApi(APIView):
    """ View for the Client management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """ Creates a new client in the platform

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "name": {"required": True, "type": "string", "empty": False},
            "phone": {
                "required": True, "type": "string",
                "empty": False, "regex": PHONE_REGEX
            },
            "email": {
                "required": True, "type": "string",
                "empty": False, "regex": EMAIL_REGEX
            }
        })
        if not validator.validate(request.data):
            return Response({
                "code": "Invalid data",
                "detailed": "Cuerpo con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        if Client.objects.filter(
            email=request.data["email"]
        ).exists():
            return Response(
                CLIENT_ALREADY_EXISTS,
                status=status.HTTP_400_BAD_REQUEST
            )

        client = Client.objects.create(
            name=request.data["name"],
            email=request.data["email"],
            phone=request.data["phone"]
        )

        return Response({
            "inserted": client.pk
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        """ Returns the Client's information

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        clients = Client.objects.all()

        return Response({
            "count": clients.count(),
            "data": paginate(
                ClientSerializer(clients, many=True).data,
                request.headers
            )
        }, status=status.HTTP_200_OK)


class SpecificClientApi(APIView):
    """ View for the Client management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, client_id):
        """ Returns the Client's information

        Parameters:
            request: The request object

            client_id: Client primary key

        Returns:
            Response: Response and status code.

        """
        client = Client.objects.filter(pk=client_id).first()

        if not client:
            return Response(CLIENT_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        return Response(
            ClientSerializer(client).data,
            status=status.HTTP_200_OK
        )

    def put(self, request, client_id):
        """ Updates the Client's information

        Parameters:
            request: The request object

            client_id: Client primary key

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "name": {"required": False, "type": "string", "empty": False},
            "phone": {
                "required": False, "type": "string",
                "empty": False, "regex": PHONE_REGEX
            },
            "email": {
                "required": False, "type": "string",
                "empty": False, "regex": EMAIL_REGEX
            }
        })
        if not request.data or not validator.validate(request.data):
            return Response({
                "code": "Invalid_body",
                "detailed": "Cuerpo con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        if "email" in request.data and Client.objects.filter(
            email=request.data["email"]
        ).exclude(pk=client_id).exists():
            return Response(
                CLIENT_ALREADY_EXISTS,
                status=status.HTTP_400_BAD_REQUEST
            )

        client = Client.objects.filter(pk=client_id)
        if not client.exists():
            return Response(CLIENT_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        client.update(**request.data)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, client_id):
        """ Deletes the Client's information

        Parameters:
            request: The request object

            client_id: Client primary key

        Returns:
            Response: Response and status code.

        """
        client = Client.objects.filter(pk=client_id).first()

        if not client:
            return Response(CLIENT_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        client.delete()

        return Response(status=status.HTTP_200_OK)

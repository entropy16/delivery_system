""" Contains the Delivery views definition. """
from cerberus import Validator

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from delivery_system.helpers.auth import CustomTokenAuthentication
from delivery_system.helpers.paginator import paginate

from delivery_system.models.client import Client
from delivery_system.models.delivery import Delivery

from delivery_system.serializers.delivery import DeliverySerializer

from delivery_system.views.client import CLIENT_NOT_FOUND

INFORMATION = "information"
CREATED_BY = "created_by"

DELIVERY_NOT_FOUND = {
    "code": "delivery_not_found",
    "detailed": "No se ha encontrado la entrega"
}


class DeliveryApi(APIView):
    """ View for the CEDI management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """ Creates a new Delivery in the platform

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "client_id": {"required": True, "type": "integer", "empty": False},
            "latitude": {"required": True, "type": "float", "empty": False},
            "longitude": {"required": True, "type": "float", "empty": False}
        })
        if not validator.validate(request.data):
            return Response({
                "code": "Invalid data",
                "detailed": "Cuerpo con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        client = Client.objects.filter(pk=request.data["client_id"]).first()
        if not client:
            return Response(CLIENT_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        delivery = Delivery.objects.create(
            client=client,
            created_by=request.user,
            latitude=request.data["latitude"],
            longitude=request.data["longitude"]
        )

        is_valid = delivery.set_cedi()
        if not is_valid:
            delivery.delete()
            return Response({
                "code": "cedi_assignment_error",
                "detailed": (
                    "Ocurrió un error al asignar el Centro de distribución"
                )
            }, status=status.HTTP_409_CONFLICT)

        return Response({
            "inserted": delivery.pk
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        """ Returns the deliveries information

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        deliveries = Delivery.objects.all()

        return Response({
            "count": deliveries.count(),
            "data": paginate(
                DeliverySerializer(deliveries, many=True).data,
                request.headers
            )
        }, status=status.HTTP_200_OK)


class SpecificDeliveryApi(APIView):
    """ View for the CEDI management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, delivery_id):
        """ Returns the cedi's information

        Parameters:
            request: The request object

            delivery_id: Delivery primary key

        Returns:
            Response: Response and status code.

        """
        delivery = Delivery.objects.filter(pk=delivery_id).first()
        if not delivery:
            return Response(
                DELIVERY_NOT_FOUND,
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            DeliverySerializer(delivery).data,
            status=status.HTTP_200_OK
        )

    def put(self, request, delivery_id):
        """ Updates the delivery's information

        Parameters:
            request: The request object

            delivery_id: Delivery primary key

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "latitude": {"required": False, "type": "float", "empty": False},
            "longitude": {"required": False, "type": "float", "empty": False}
        })
        if not request.data or not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": "Cuerpo con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        delivery = Delivery.objects.filter(pk=delivery_id)
        if not delivery.exists():
            return Response(DELIVERY_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        delivery.update(**request.data)

        is_valid = delivery.first().set_cedi()
        if not is_valid:
            return Response({
                "code": "cedi_assignment_error",
                "detailed": (
                    "Ocurrió un error al asignar el Centro de distribución"
                )
            }, status=status.HTTP_409_CONFLICT)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, delivery_id):
        """ Deletes the cedi's information

        Parameters:
            request: The request object

            delivery_id: Delivery primary key

        Returns:
            Response: Response and status code.

        """
        delivery = Delivery.objects.filter(pk=delivery_id).first()

        if not delivery:
            return Response(DELIVERY_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        delivery.delete()

        return Response(status=status.HTTP_200_OK)

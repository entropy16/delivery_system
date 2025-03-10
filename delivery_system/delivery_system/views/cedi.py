""" Contains the CEDI views definition. """
from cerberus import Validator

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from delivery_system.helpers.paginator import paginate
from delivery_system.helpers.auth import CustomTokenAuthentication

from delivery_system.models.cedi import CEDI

from delivery_system.serializers.cedi import CEDISerializer

INFORMATION = "information"
METRICS = "metrics"

CEDI_NOT_FOUND = {
    "code": "cedi_not_found",
    "detailed": "No se ha encontrado el centro de distribución"
}

CEDI_NAME_ALREADY_EXISTS = {
    "code": "cedi_already_exists",
    "detailed": "Ya existe un centro de distribución con ese nombre"
}

CEDI_UBICATION_ALREADY_EXISTS = {
    "code": "cedi_already_exists",
    "detailed": "Ya existe un centro de distribución con esa ubicación"
}


class CEDIApi(APIView):
    """ View for the CEDI management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """ Creates a new cedi in the platform

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "name": {"required": True, "type": "string", "empty": False},
            "latitude": {"required": True, "type": "float", "empty": False},
            "longitude": {"required": True, "type": "float", "empty": False}
        })
        if not validator.validate(request.data):
            return Response({
                "code": "Invalid data",
                "detailed": "Cuerpo con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        if CEDI.objects.filter(
            name=request.data["name"]
        ).exists():
            return Response(
                CEDI_NAME_ALREADY_EXISTS,
                status=status.HTTP_400_BAD_REQUEST
            )

        if CEDI.objects.filter(
            latitude=request.data["latitude"],
            longitude=request.data["longitude"]
        ).exists():
            return Response(
                CEDI_UBICATION_ALREADY_EXISTS,
                status=status.HTTP_400_BAD_REQUEST
            )

        cedi = CEDI.objects.create(
            name=request.data["name"],
            latitude=request.data["latitude"],
            longitude=request.data["longitude"]
        )

        return Response({
            "inserted": cedi.pk
        }, status=status.HTTP_201_CREATED)

    def get(self, request):
        """ Returns the cedi's information

        Parameters:
            request: The request object

        Returns:
            Response: Response and status code.

        """
        cedi = CEDI.objects.all()

        return Response({
            "count": cedi.count(),
            "data": paginate(
                CEDISerializer(cedi, many=True).data,
                request.headers
            )
        }, status=status.HTTP_200_OK)


class SpecificCEDIApi(APIView):
    """ View for the CEDI management """
    authentication_classes = [CustomTokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, cedi_id):
        """ Returns the cedi's information

        Parameters:
            request: The request object

            cedi_id: CEDI primary key

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "action": {
                "required": True, "type": "string",
                "allowed": [INFORMATION, METRICS]
            }
        })
        if not validator.validate(request.query_params):
            return Response({
                "code": "invalid_query",
                "detailed": "Query con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        cedi = CEDI.objects.filter(pk=cedi_id).first()

        if not cedi:
            return Response(CEDI_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        data = {}
        if request.query_params["action"] == INFORMATION:
            data = CEDISerializer(cedi).data

        elif request.query_params["action"] == METRICS:
            data = cedi.get_metrics()

        return Response(data, status=status.HTTP_200_OK)

    def put(self, request, cedi_id):
        """ Updates the cedi's information

        Parameters:
            request: The request object

            cedi_id: CEDI primary key

        Returns:
            Response: Response and status code.

        """
        validator = Validator({
            "name": {"required": False, "type": "string", "empty": False},
            "latitude": {"required": False, "type": "float", "empty": False},
            "longitude": {"required": False, "type": "float", "empty": False}
        })
        if not request.data or not validator.validate(request.data):
            return Response({
                "code": "invalid_body",
                "detailed": "Cuerpo con estructura inválida",
                "errors": validator.errors
            }, status=status.HTTP_400_BAD_REQUEST)

        if "name" in request.data and CEDI.objects.filter(
            name=request.data["name"]
        ).exclude(pk=cedi_id).exists():
            return Response(
                CEDI_NAME_ALREADY_EXISTS,
                status=status.HTTP_400_BAD_REQUEST
            )

        if CEDI.objects.filter(
            latitude=request.data.get("latitude", None),
            longitude=request.data.get("longitude", None)
        ).exclude(pk=cedi_id).exists():
            return Response(
                CEDI_UBICATION_ALREADY_EXISTS,
                status=status.HTTP_400_BAD_REQUEST
            )

        cedi = CEDI.objects.filter(pk=cedi_id)
        if not cedi.exists():
            return Response(CEDI_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        cedi.update(**request.data)

        return Response(status=status.HTTP_200_OK)

    def delete(self, request, cedi_id):
        """ Deletes the cedi's information

        Parameters:
            request: The request object

            cedi_id: CEDI primary key

        Returns:
            Response: Response and status code.

        """
        cedi = CEDI.objects.filter(pk=cedi_id).first()

        if not cedi:
            return Response(CEDI_NOT_FOUND, status=status.HTTP_404_NOT_FOUND)

        cedi.delete()

        return Response(status=status.HTTP_200_OK)

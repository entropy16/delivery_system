============================
 Delivery API Documentation
============================

Este documento describe los endpoints de la API para las operaciones relacionadas con las entregas en el sistema de entrega.

Crear Entrega
-------------

.. http:post:: /api/delivery

    Crea un nuevo Centro de Distribución en la plataforma

**Request Body:**

.. sourcecode:: http

    POST /api/delivery HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "client_id": 1,
        "latitude": 94.123,
        "longitude": -94.123
    }

**Responses:**

Entrega registrada con éxito

.. sourcecode:: http

    HTTP/1.1 201 CREATED
    Content-Type: application/json

    {
        "inserted": 7
    }

.. sourcecode:: http

    HTTP/1.1 400 BAD REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detailed": "Cuerpo con estructura inválida",
        "error": {}
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "client_not_found",
        "detailed": "No se ha encontrado el cliente"
    }

.. sourcecode:: http

    HTTP/1.1 409 CONFLICT
    Content-Type: application/json

    {
        "code": "cedi_assignment_error",
        "detailed": "Ocurrió un error al asignar el Centro de distribución"
    }


Obtener Entregas
----------------

.. http:get:: /api/delivery

    Obtiene la información de las entregas registradas en el sistema

**Request Body:**

.. sourcecode:: http

    GET /api/delivery HTTP/1.1
    Authorization: Bearer <token>

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "count": 17,
        "data": [
            {
                "id": 18,
                "client": "Cliente Apellido",
                "cedi": "Archivo 2",
                "distance": 18.834,
                "estimated_duration": 31.366666666666667,
                "latitude": 4.796599925735624,
                "longitude": -75.68323670981594,
                "created": "2025-03-10T04:40:00.467539Z"
            },
            {
                "id": 17,
                "client": "Cliente Apellido",
                "cedi": "Archivo 2",
                "distance": 18.834,
                "estimated_duration": 0.016666666666666666,
                "latitude": 4.796599925735624,
                "longitude": -75.68323670981594,
                "created": "2025-03-10T04:38:14.246749Z"
            },
            {
                "id": 16,
                "client": "Cliente Apellido",
                "cedi": "Archivo 2",
                "distance": 18.834,
                "estimated_duration": 0.016666666666666666,
                "latitude": 4.796599925735624,
                "longitude": -75.68323670981594,
                "created": "2025-03-10T04:37:44.689599Z"
            }
        ]
    }


Obtener Entrega específica
--------------------------

.. http:get:: /api/delivery/<int:delivery_id>

    Obtiene la información de una Entrega específica

**Request Body:**

.. sourcecode:: http

    GET /api/delivery/1 HTTP/1.1
    Authorization: Bearer <token>

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "id": 1,
        "client": "Cliente Apellido",
        "cedi": "Archivo 2",
        "distance": 18.834,
        "estimated_duration": 0.016666666666666666,
        "latitude": 4.796599925735624,
        "longitude": -75.68323670981594,
        "created": "2025-03-10T04:37:44.689599Z"
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "delivery_not_found",
        "detailed": "No se ha encontrado la entrega"
    }


Actualizar Entrega
------------------

.. http:put:: /api/delivery/<int:delivery_id>

    Actualiza la información de una Entrega específica

**Request Body:**

.. sourcecode:: http

    PUT /api/delivery HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "latitude": -94.123,
        "longitude": 94.123,
    }

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

.. sourcecode:: http

    HTTP/1.1 400 BAD REQUEST
    Content-Type: application/json

    {
        "code": "invalid_body",
        "detailed": "Cuerpo con estructura inválida",
        "error": {}
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "delivery_not_found",
        "detailed": "No se ha encontrado la entrega"
    }

.. sourcecode:: http

    HTTP/1.1 409 CONFLICT
    Content-Type: application/json

    {
        "code": "cedi_assignment_error",
        "detailed": "Ocurrió un error al asignar el Centro de distribución"
    }


Borrar Entrega
--------------

.. http:delete:: /api/delivery/<int:delivery_id>

    Elimina una entrega específica

**Request Body:**

.. sourcecode:: http

    DELETE /api/delivery/3 HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "delivery_not_found",
        "detailed": "No se ha encontrado la entrega"
    }

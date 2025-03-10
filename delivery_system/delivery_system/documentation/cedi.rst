========================
 CEDI API Documentation
========================

Este documento describe los endpoints de la API para las operaciones relacionadas con los CEDI en el sistema de entrega.

Crear CEDI
----------

.. http:post:: /api/cedi

    Crea un nuevo Centro de Distribución en la plataforma

**Request Body:**

.. sourcecode:: http

    POST /api/cedi HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "name": "string",
        "latitude": 94.123,
        "longitude": -94.123,
    }

**Responses:**

CEDI registrado con éxito

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
    
    {
        "code": "cedi_already_exists",
        "detailed": "Ya existe un centro de distribución con ese nombre"
    }

    {
        "code": "cedi_already_exists",
        "detailed": "Ya existe un centro de distribución con esa ubicación"
    }


Obtener CEDI
------------

.. http:get:: /api/cedi

    Obtiene la información de todos los CEDI registrados en el sistema. según el campo "action"

**Request Body:**

.. sourcecode:: http

    GET /api/cedi?action=information HTTP/1.1
    Authorization: Bearer <token>

    GET /api/cedi?action=metrics HTTP/1.1
    Authorization: Bearer <token>

    GET /api/cedi?action=by_delivery_type HTTP/1.1
    Authorization: Bearer <token>

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    **action = information**

    {
        "count": 4,
        "data": [
            {
                "id": 1,
                "name": "Centro De la ciudad",
                "latitude": 4.533097713035964,
                "longitude": -75.66932206714714
            },
            {
                "id": 2,
                "name": "Centro de la ciudad",
                "latitude": 4.084463697811905,
                "longitude": -76.19807848856205
            },
            {
                "id": 4,
                "name": "Centro 11",
                "latitude": 4.870547426225461,
                "longitude": -72.88639353338444
            },
            {
                "id": 5,
                "name": "Archivo 2",
                "latitude": 4.8542450156367725,
                "longitude": -75.62461180141233
            }
        ]
    }

    **action = metrics**

    {
        "count": 4,
        "data": [
            {
                "id": 1,
                "name": "Centro De la ciudad",
                "metrics": {
                    "min_distance": null,
                    "max_distance": null,
                    "min_duration": null,
                    "max_duration": null,
                    "avg_speed": null,
                    "avg_min_per_km": null
                }
            },
            {
                "id": 2,
                "name": "Centro de la ciudad",
                "metrics": {
                    "min_distance": null,
                    "max_distance": null,
                    "min_duration": null,
                    "max_duration": null,
                    "avg_speed": null,
                    "avg_min_per_km": null
                }
            },
            {
                "id": 4,
                "name": "Centro 11",
                "metrics": {
                    "min_distance": 192.678,
                    "max_distance": 192.678,
                    "min_duration": 243.31666666666666,
                    "max_duration": 243.31666666666666,
                    "avg_speed": 47.512898143708476,
                    "avg_min_per_km": 1.2628149901216883
                }
            },
            {
                "id": 5,
                "name": "Archivo 2",
                "metrics": {
                    "min_distance": 18.834,
                    "max_distance": 18834.0,
                    "min_duration": 0.016666666666666666,
                    "max_duration": 31.366666666666667,
                    "avg_speed": 57637.43541644564,
                    "avg_min_per_km": 0.0010409901059352175
                }
            }
        ]
    }

    **action = by_delivery_type**

    {
        "count": 4,
        "data": [
            {
                "id": 1,
                "name": "Centro De la ciudad",
                "deliveries": {
                    "normal": 0,
                    "express": 0
                }
            },
            {
                "id": 2,
                "name": "Centro de la ciudad",
                "deliveries": {
                    "normal": 0,
                    "express": 0
                }
            },
            {
                "id": 4,
                "name": "Centro 11",
                "deliveries": {
                    "normal": 1,
                    "express": 0
                }
            },
            {
                "id": 5,
                "name": "Archivo 2",
                "deliveries": {
                    "normal": 1,
                    "express": 3
                }
            }
        ]
    }


Obtener CEDE específico
-----------------------

.. http:get:: /api/cedi/<int:cedi_id>

    Obtiene la información de un CEDI específico

**Request Body:**

.. sourcecode:: http

    GET /api/cedi/1 HTTP/1.1
    Authorization: Bearer <token>

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "id": 1,
        "name": "Centro De la ciudad",
        "latitude": 4.533097713035964,
        "longitude": -75.66932206714714
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "cedi_not_found",
        "detailed": "No se ha encontrado el centro de distribución"
    }


Actualizar CEDI
---------------

.. http:put:: /api/cedi/<int:cedi_id>)

    Actualiza la información de un CEDI específico

**Request Body:**

.. sourcecode:: http

    PUT /api/cedi HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "name": "string",
        "latitude": 94.123,
        "longitude": -94.123,
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

    {
        "code": "cedi_already_exists",
        "detailed": "Ya existe un centro de distribución con ese nombre"
    }

    {
        "code": "cedi_already_exists",
        "detailed": "Ya existe un centro de distribución con esa ubicación"
    }


Borrar CEDI
-----------

.. http:delete:: /api/cedi/<int:cedi_id>

   Delete the authenticated user's account.

**Request Body:**

.. sourcecode:: http

    DELETE /api/cedi HTTP/1.1
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
        "code": "cedi_not_found",
        "detailed": "No se ha encontrado el centro de distribución"
    }

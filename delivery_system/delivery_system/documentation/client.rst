==========================
 Client API Documentation
==========================

Este documento describe los endpoints de la API para las operaciones relacionadas con los Clientes en el sistema de entrega.

Crear Cliente
-------------

.. http:post:: /api/client

    Crea un nuevo Centro de Distribución en la plataforma

**Request Body:**

.. sourcecode:: http

    POST /api/client HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "name": "string",
        "phone": "string",
        "email": "string"
    }

**Responses:**

Cliente registrado con éxito

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
        "code": "client_already_exists",
        "detailed": "Ya existe un cliente con ese correo electrónico"
    }


Obtener Cliente
---------------

.. http:get:: /api/client

    Obtiene la información de los clientes registrados en el sistema

**Request Body:**

.. sourcecode:: http

    GET /api/client HTTP/1.1
    Authorization: Bearer <token>

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "count": 6,
        "data": [
            {
                "id": 1,
                "name": "Cliente Apellido",
                "phone": "3231232321",
                "email": "client1@yopmail.com"
            },
            {
                "id": 2,
                "name": "Cliente 1",
                "phone": "3231232321",
                "email": "client2@yopmail.com"
            },
            {
                "id": 4,
                "name": "Cliente 1",
                "phone": "3231232321",
                "email": "client4@yopmail.com"
            }
        ]
    }


Obtener Cliente específico
--------------------------

.. http:get:: /api/client/<int:client_id>

    Obtiene la información de un Cliente específico

**Request Body:**

.. sourcecode:: http

    GET /api/client/1 HTTP/1.1
    Authorization: Bearer <token>

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "id": 1,
        "name": "Cliente Apellido",
        "phone": "3231232321",
        "email": "prueba@gmail.com"
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "client_not_found",
        "detailed": "No se ha encontrado el cliente"
    }


Actualizar Cliente
------------------

.. http:put:: /api/client/<int:client_id>

    Actualiza la información de un Cliente específico

**Request Body:**

.. sourcecode:: http

    PUT /api/client HTTP/1.1
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
        "code": "client_already_exists",
        "detailed": "Ya existe un cliente con ese correo electrónico"
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "client_not_found",
        "detailed": "No se ha encontrado el cliente"
    }


Borrar Cliente
--------------

.. http:delete:: /api/client/<int:client_id>

    Elimina un cliente específico

**Request Body:**

.. sourcecode:: http

    DELETE /api/client/3 HTTP/1.1
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
        "code": "client_not_found",
        "detailed": "No se ha encontrado el cliente"
    }


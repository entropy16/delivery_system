========================
 User API Documentation
========================

Este documento describe los endpoints de la API para las operaciones relacionadas con los Usuarios en el sistema de entrega.

Registrar Usuario
-----------------

.. http:post:: /api/user/register

    Crea un nuevo usuario en la plataforma

**Request Body:**

.. sourcecode:: http

    POST /api/user/register HTTP/1.1
    Content-Type: application/json

    {
        "username": "string",
        "email": "string",
        "password": "string"
    }

**Responses:**

Usuario registrado con éxito

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
        "username": [
            "A user with that username already exists."
        ]
    }


Obtener Usuarios
----------------

.. http:get:: /api/user

    Obtiene la lista de usuarios registrados en la plataforma.

**Request Body:**

.. sourcecode:: http

    GET /api/user HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    [
        {
            "id": 1,
            "username": "admin",
            "email": "admin@yopmail.com"
        },
        {
            "id": 4,
            "username": "user31",
            "email": "user21@yopmail.com"
        },
        {
            "id": 6,
            "username": "user3",
            "email": "user3@yopmail.com"
        },
        {
            "id": 7,
            "username": "user2",
            "email": "user3@yopmail.com"
        }
    ]


Actualizar Usuario
------------------

.. http:put:: /api/user

    Actualiza la información del usuario autenticado.

**Request Body:**

.. sourcecode:: http

    PUT /api/user HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

    {
        "username": "string",
        "email": "string"
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
        "code": "user_already_exists",
        "detailed": "Ya existe un usuario con ese username y/o email"
    }


Borrar Usuario
--------------

.. http:delete:: /api/user

    Elimina la cuenta del usuario autenticado.

**Request Body:**

.. sourcecode:: http

    DELETE /api/user HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json


Obtener Entregas por Usuario
----------------------------

.. http:get:: /api/user/delivery

    Obtiene la información de entregas creadas por los usuarios.

**Request Body:**

.. sourcecode:: http

    GET /api/user/delivery HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

    {
        "count": 4,
        "data": [
            {
                "id": 6,
                "username": "user3",
                "deliveries_count": 17
            },
            {
                "id": 1,
                "username": "admin",
                "deliveries_count": 15
            },
            {
                "id": 7,
                "username": "user2",
                "deliveries_count": 5
            },
            {
                "id": 4,
                "username": "user31",
                "deliveries_count": 0
            }
        ]
    }

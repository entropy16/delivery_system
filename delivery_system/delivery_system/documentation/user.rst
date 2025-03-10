========================
 User API Documentation
========================

This document describes the API endpoints for user-related operations in the delivery system.

Register User
-------------

.. http:post:: /api/user/register

   Register a new user account.

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


Get Users
---------

.. http:get:: /api/user

   Retrieves all users information.

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


Update User Profile
-------------------

.. http:put:: /api/user

   Update the authenticated user's profile information.

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


Delete User Account
-------------------

.. http:delete:: /api/user

   Delete the authenticated user's account.

**Request Body:**

.. sourcecode:: http

    DELETE /api/user HTTP/1.1
    Authorization: Bearer <token>
    Content-Type: application/json

**Response:**

.. sourcecode:: http

    HTTP/1.1 200 OK
    Content-Type: application/json

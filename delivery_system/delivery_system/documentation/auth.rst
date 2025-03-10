========================
 Auth API Documentation
========================

This document describes the API endpoints for authentication-related operations in the delivery system.

Login
-----

.. http:post:: /api/auth

    Authenticate a user.

**Request Body:**

.. sourcecode:: http

    POST /api/auth HTTP/1.1
    Content-Type: application/json

    {
        "username": "string",
        "password": "string"
    }

**Response:**

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
        "code": "invalid_password",
        "detailed": "Contraseña incorrecta"
    }

.. sourcecode:: http

    HTTP/1.1 404 NOT FOUND
    Content-Type: application/json

    {
        "code": "user_not_found",
        "detailed": "Usuario no encontrado"
    }

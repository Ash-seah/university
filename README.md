# University Project: FastAPI Phonebook

## Overview

This project is a simple phonebook application built using FastAPI. It includes user authentication (login and registration) and manages different classes and their associated tables.

## Features

User Registration and Login

CRUD operations for classes and associated tables (Teachers, Tajrobi, Riazi, Ensani)

Secure password handling with hashing

JWT token-based authentication

## Usage

User Registration

Endpoint: /register/

Method: POST


User Login

Endpoint: /login/

Method: POST

## Classes

Create: POST /classes/

Read: GET /classes/{id}/

Update: PUT /classes/{id}/

Delete: DELETE /classes/{id}/
Teachers, Tajrobi, Riazi, Ensani

Similar CRUD endpoints as for classes, replacing /classes/ with the respective table name.

## Database Schema
Classes Table: Stores class information.

Teachers Table: Stores teacher information, with a foreign key to the classes table.

Tajrobi Table: Stores information specific to Tajrobi, with a foreign key to the classes table.

Riazi Table: Stores information specific to Riazi, with a foreign key to the classes table.

Ensani Table: Stores information specific to Ensani, with a foreign key to the classes table.

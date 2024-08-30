# Document Collaboration System

## Overview

The Document Collaboration System is a Django-based web application designed to facilitate document management and collaboration within an organization. This application provides functionalities for managing documents, tasks, user roles, and privileges, with a focus on seamless integration and performance.

## Key Features

- **RESTful APIs**: Provides a set of APIs for managing documents, tasks, and user profiles.
- **PostgreSQL Database**: Utilizes PostgreSQL for robust and scalable data management.
- **Redis Caching**: Implements Redis for efficient caching and improved performance.
- **Django Signals**: Uses Django signals to handle asynchronous events and notifications.

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- Django 4.x
- PostgreSQL
- Redis

### Installation Steps

1. **Clone the Repository**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
2. **Create and Activate a Virtual Environment**

    ```bash

    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
3. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
4. **Configure PostgreSQL**

Update the DATABASES settings in core/settings.py with your PostgreSQL database credentials.

5. **Configure Redis**

Update the CACHES settings in core/settings.py with your Redis server details.

6. **Apply Migrations**
    ```bash
    python manage.py migrate


7. **Load Initial Data**

Generate and load sample data:

    ```bash

    python generate_data.py
    python manage.py loaddata documents_data.json
    python manage.py loaddata tasks_data.json
8. **Run the Development Server**

    ```bash
    python manage.py runserver
## RESTful APIs

### Document Endpoints

- **List Documents**

  `GET /api/documents/`

  Retrieves a list of all documents.

- **Create Document**

  `POST /api/documents/`

  Creates a new document. Requires fields: `title`, `content`, `collaborators`, `created_by`.

- **Retrieve Document**

  `GET /api/documents/{id}/`

  Retrieves a specific document by ID.

- **Update Document**

  `PUT /api/documents/{id}/`

  Updates a specific document by ID.

- **Delete Document**

  `DELETE /api/documents/{id}/`

  Deletes a specific document by ID.

### Task Endpoints

- **List Tasks**

  `GET /api/tasks/`

  Retrieves a list of all tasks.

- **Create Task**

  `POST /api/tasks/`

  Creates a new task. Requires fields: `title`, `description`, `assigned_users`, `status`.

- **Retrieve Task**

  `GET /api/tasks/{id}/`

  Retrieves a specific task by ID.

- **Update Task**

  `PUT /api/tasks/{id}/`

  Updates a specific task by ID.

- **Delete Task**

  `DELETE /api/tasks/{id}/`

  Deletes a specific task by ID.

## PostgreSQL Database

The application uses PostgreSQL for data storage. The database schema is defined in the Django models within the `documents` and `tasks` apps. To interact with PostgreSQL:

- **Admin Interface**: Access the Django admin interface at `/admin/` to manage data through the web UI.
- **Database Management**: Use tools like pgAdmin or command-line utilities to interact with the PostgreSQL database directly.

## Redis Caching

Redis is used to cache frequent queries and data to enhance performance. The caching configuration is defined in `core/settings.py`. Key caching strategies include:

- **Document Caching**: Cache document queries to reduce database load.
- **Task Caching**: Cache task queries for improved response times.

## Django Signals

Django signals are used to handle asynchronous events and notifications. Key signals in this project include:

- **Document Creation Signal**: Triggered when a new document is created to perform additional actions, such as notifications.
- **Task Assignment Signal**: Triggered when a task is assigned to a user to update related data or notify the user.

License
This project is licensed under the MIT License. See the LICENSE file for details.

# Portfolio Project

This project is a collection of random Django-based web applications. 

## Setup Guide

### Prerequisites

- Python 3.x
- Django
- PostgreSQL
- psycopg2 (PostgreSQL adapter for Python)

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/holy-alexis/portfolio
    cd portfolio
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Database Setup

1. Create a PostgreSQL database named `towns`:
    ```sql
    CREATE DATABASE towns WITH OWNER postgres ENCODING 'utf-8';
    ```

2. Update the `settings.py` file to configure the database connection:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'towns',
            'USER': 'your_db_user',
            'PASSWORD': 'your_db_password',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    ```

### Load Initial Data

1. Load the initial data for the `Towns` app using `make.py`:
    ```bash
    python make.py
    ```

### Create a Superuser

1. Create a superuser to access the Django admin interface:
    ```bash
    python manage.py createsuperuser
    ```

2. Follow the prompts to set up the superuser account.

## Running the Application

1. Start the development server:
    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://127.0.0.1:8000/` to view the application.

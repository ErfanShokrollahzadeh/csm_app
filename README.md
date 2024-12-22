# CSM App

## Overview

The CSM App is a web application that provides a platform for users to manage their accounts, view posts, and interact with various features. The application is built using Django for the backend and Vue.js for the frontend. Docker is used for containerization to simplify the setup and deployment process.

## Features

- User registration and authentication
- Post creation and management
- Category management
- Onboarding information
- Country selection
- Topic management
- News source management
- Profile management

## Setup Instructions

### Django Backend

1. Clone the repository:
   ```bash
   git clone https://github.com/ErfanShokrollahzadeh/csm_app.git
   cd csm_app
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply the database migrations:
   ```bash
   python manage.py migrate
   ```

5. Create a superuser account:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

### Vue.js Frontend

1. Navigate to the `app/vueapp` directory:
   ```bash
   cd app/vueapp
   ```

2. Install the required dependencies:
   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run serve
   ```

### Using Docker

1. Build and start the Docker containers:
   ```bash
   docker-compose up --build
   ```

2. Access the Django backend at `http://localhost:8000` and the Vue.js frontend at `http://localhost:8080`.

## Running Tests

### Django Backend

1. Ensure the virtual environment is activated.
2. Run the tests:
   ```bash
   python manage.py test
   ```

### Vue.js Frontend

1. Navigate to the `app/vueapp` directory:
   ```bash
   cd app/vueapp
   ```

2. Run the tests:
   ```bash
   npm run test
   ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

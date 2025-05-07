# country_details

## Installation
Follow the steps below to get this project up and running on your local machine.

## Requirements
Python 3.10+

pip (Python package manager)

Git (optional, for cloning the repo)

## Setup Instructions
Create and activate a virtual environment
    `python -m venv venv`
    `source venv/bin/activate`      # For Linux/macOS
    `venv\Scripts\activate`       # For Windows


### Install dependencies:
This project uses Django 5 and Django REST Framework. All required packages are listed in requirements.txt. Install them with:
    `pip install -r requirements.txt`

### Apply database migrations:
`python manage.py makemigrations`
`python manage.py migrate`

### Create a superuser account:
This is used to access the Django admin panel.
    `python manage.py createsuperuser`


### Access the application:
Open your browser and go to http://127.0.0.1:8000/ to view the app.
Go to http://127.0.0.1:8000/admin/ to access the admin panel.
Go to http://127.0.0.1:8000/api/<API endpoints> to access the API endpoints.

### Tech Stack
Python 3.10+
Django 5
Django REST Framework – Used for building secure and modular API endpoints.
SQLite – Default database (can be replaced with PostgreSQL or others).



# Authentication
This project uses Django’s built-in authentication system to access certain pages and Django Rest Framework to restrict accesss to API endpoints.

### Login (via Web)
Visit the login page at:
http://localhost:8000/login/

Use a registered username and password to log in.

After login, users are redirected to the home page.

### Logout
To log out, click the Logout button in the navigation bar.
You will be redirected to the login page.


# Accessing API endpoints
### Obtain Token
    Endpoint:
    POST http://127.0.0.1:8000/api/api-token-auth/

    Headers: `Content-Type: application/x-www-form-urlencoded`
    Body (form-data or x-www-form-urlencoded): 
```
    username=your_username
    password=your_password
```

    Response from the server:
    ```
    {
        "token": "your_generated_token"
    }
    ```

### Use the Token in API Requests
Once you obtain the token, include it in the Authorization header of subsequent API requests:
Header: `Authorization: Token your_generated_token`

Example with curl:
`curl -H "Authorization: Token your_generated_token" http://127.0.0.1:8000/api/country-details/bgd/`




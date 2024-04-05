# Scoring Management System:

Develop a RESTful API using Django and Django REST Framework to manage score ,
incorporating Sqlite, for data storage, and implementing a role-based access control system.

# Local Setup-

git clone url
pip install -r requirements.txt

Run migration commands:
 python manage.py makemigrations
 python manage.py migrate

To run the server and check all API endpoints:
 python manage.py runserver

To create a superuser, use the following command: 
    python manage.py createsuperuser


# Check the admin interface-

    http://0.0.0.0:8000/admin

# Check the swagger documentation-

    http://0.0.0.0:8000/api/schema/swagger-ui/

# Tech Stack

python
DRF
sqliteDB
swagger
JWT
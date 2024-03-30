Django Social Network
Django Social Network is a web application built with Django that allows users to send, accept, and reject friend requests, list friends, and manage pending friend requests.

Installation
Prerequisites
Python (version 3.6 or higher)
Django (version 3.2 or higher)
Django Rest Framework (version 3.12 or higher)
Other dependencies specified in requirements.txt
Installation Steps
Clone the repository:- https://github.com/saurabh-kr0807/django_rest_api_demo/
Navigate to the project directory:- cd social_network
Activate the virtual environment:(django_rest_demo) if not create the new virtual environment :- source env/bin/activate or source django_rest_demo/bin/activate
Install dependencies:- pip install -r requirements.txt
Perform database migrations:- python manage.py migrate
Run the development server:- python manage.py runserver (Access the application in your web browser at http://localhost:8000/)
if you need to run the docker then please install docker into the system and run the command:- docker-compose up --build (Access the application in your web browser at http://localhost:8000/)

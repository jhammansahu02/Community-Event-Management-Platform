# Community Event Management System
A Django-based application designed to help users create, manage, and RSVP to community events. The system allows event organizers to create events, manage categories, and users to register, log in, and RSVP to events.

# Features
1. User Authentication: Users can sign up, log in, and manage their account details.
2. Event Management: Organizers can create, update, and delete events.
3. RSVP System: Users can RSVP to events, and organizers can set RSVP limits.
4. Categories: Events can be categorized, making it easier for users to find relevant events.
5. Role-based Access: Admins have full access to all functionalities, while regular users can only manage their own events and RSVPs.

# Technologies Used
Django 5.1.3
Django Rest Framework for building APIs
JWT (JSON Web Token) for secure authentication
SQLite (for development) or any other relational database
Python 3.11 (or higher)

# Installation
Prerequisites
Python 3.11 or higher
Django 5.1.3 or higher
pip (Python package manager)

# Steps

1. Clone the repository:
    git clone https://github.com/jhammansahu02/Community-Event-Management-Platform.git
    
    cd Community-Event-Management-Platform

2. Setup vertual environment:
     python3 -m venv env
    # On Linux, use `source env/bin/activate`
    # On Windows, use `venv\Scripts\activate`

    cd backend 

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations to set up the database:
    python manage.py migrate    

5. Create a superuser to access the admin panel:
    python manage.py createsuperuser

6. Start the development server:
    python manage.py runserver   

7. Press Ctrl + Z to suspend the current process (this will stop the server temporarily).
   Run the command bg to resume the process in the background.


# How to use application

<!-- To Signup use these data to test -->

    curl -X POST http://127.0.0.1:8000/api/v1/signup/ \
    -H "Content-Type: application/json" \
    -d '{"password": "12345", "email": "rey@gmail.com", "first_name":"Rey", "last_name":"sarva","contact_number":"9098909890", "gender":"M"}'

    Resonse:
    {"success":"Registration done successfully","username":"rey@gmail.com"}
<!-- To Signup use these data to test -->   

<!-- To login -->
    curl -X POST http://127.0.0.1:8000/api/v1/login/ \
    -H "Content-Type: application/json" \
    -d '{"username": "rey@gmail.com", "password": "12345"}'

    Response:
    {"success":"Login successful","refresh":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTczNDI3NDcyOCwiaWF0IjoxNzMxNjgyNzI4LCJqdGkiOiJkM2I2OGVhZTRhN2Q0MDRjYmEyZTFkMmRiMTlkZTY4NCIsInVzZXJfaWQiOjJ9.9k8RCB1XeeI2aj7uvMBZdITBUDs8hO5clLzsQI-fmW0","access":"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzMxNzY5MTI4LCJpYXQiOjE3MzE2ODI3MjgsImp0aSI6IjJkM2RjZjJmMWNiODRlNTQ4OTQ3MWU2NmIzYTI0OGUwIiwidXNlcl9pZCI6Mn0.l6YxMDa2XMr5pyuQbqIfvbit0SA7ju9G82vNRwt3zRc","user":{"id":2,"first_name":"Rey","last_name":"sarva","email":"rey@gmail.com"}}
<!-- To login -->

<!-- only admin can create category for event so admin have to store category from panel -->

<!-- Add events (only logged in users can create event) -->
    curl -X POST http://127.0.0.1:8000/api/v1/events/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <your-jwt-token>" \
    -d '{
        "title": "Tech Conference 2024",
        "description": "A conference on the latest in technology",
        "location": "New York City",
        "category": 1,
        "rsvp_limit": 200
    }'

    Response:
    {"success":"Event created"}
<!-- Add events (only logged in users can create event) -->

<!-- update event (only who created it) -->

    curl -X PATCH http://127.0.0.1:8000/api/v1/events/<event-id>/ \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer <your-jwt-token>" \
    -d '{
        "location": "San Francisco"
    }'

    Response:
    {"success":"Event updated"}

<!-- update event (only who created it) -->

<!-- Delete Event (only who created it) -->
    curl -X DELETE http://127.0.0.1:8000/api/v1/events/<event_id>/ \
    -H "Authorization: Bearer <your-jwt-token>"

    Response:
    {"success":"Event deleted"}
<!-- Delete Event (only who created it) -->

<!-- get one event -->
    curl -X GET http://127.0.0.1:8000/api/v1/events/<event_id>/

    Response::
    {"id":2,"title":"Tech Conference 2024","description":"A conference on the latest in technology","date":"2024-11-15","time":"15:17:53.338608","location":"New York City","organizer":{"id":2,"username":"rey@gmail.com","email":"rey@gmail.com","first_name":"Rey","last_name":"sarva","contact_number":"9098909890","gender":"M","is_staff":false,"is_superuser":false},"category":{"id":1,"name":"Technology","description":"Events related to technology and innovation"},"rsvp_limit":200} 
<!-- get one event -->

<!-- get list of event -->
    curl -X GET http://127.0.0.1:8000/api/v1/events/
<!-- get list of event -->

<!-- to RSVP for any event -->
    curl -X POST http://127.0.0.1:8000/api/v1/rsvp/<event_id>/ \
    -H "Authorization: Bearer <your-jwt-token>"

    Response:
    {"success":"RSVP successful"}
<!-- to RSVP for any event -->

# Extra details

    Admin have option to searching for events, filtering by date, category or location, and sorting options.







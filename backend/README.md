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
    git clone https://github.com/yourusername/community-event-management-system.git
    cd community-event-management-system

2. Setup vertual environment:
    python -m venv venv
    # On Windows, use `venv\Scripts\activate` 
    # On Linux, use `source venv/bin/activate`

3. Install dependencies:
    pip install -r requirements.txt

4. Apply migrations to set up the database:
    python manage.py migrate    

5. Create a superuser to access the admin panel:
    python manage.py createsuperuser

6. Start the development server:
    python manage.py runserver    

    

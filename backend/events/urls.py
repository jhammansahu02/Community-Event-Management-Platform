from django.urls import path
from .views import *

urlpatterns = [
    path('signup/', SignupAPIView.as_view()), # Added a path to signup for user
    path('login/', LoginAPIView.as_view()), # Added a path to login for user
    path('category/', CategoryAPIView.as_view()), # Added a path to create category for events
    path('events/', EventsCreateDeleteUpdateAPI.as_view()), # Added a path to create events
    path('events/<int:event_id>/', EventsCreateDeleteUpdateAPI.as_view()), # Added a path to delete or update any particuler event
    path('events-list/', EventListAPI.as_view()), # Added a path to fetch list of event
    path('events-list/<int:event_id>/', EventListAPI.as_view()), # Added a path to fetch a particular event
    path('rsvp/<int:event_id>/', RSVPAPI.as_view()), # Added a path to rsvp for any event
]

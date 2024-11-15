from django.contrib import admin
from .models import *

# Addition of code
# Reason - to register user model in admin panel
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id','username', 'email', 'first_name', 'last_name', 'gender')
# End of addition of code
# Reason - to register user model in admin panel  
  
# Addition of code
# Reason - to register event model in admin panel  
@admin.register(Event)  
class EventAdmin( admin.ModelAdmin):
    list_display = ('id','title', 'date', 'time', 'location','category', 'organizer')  
    readonly_fields = ('rsvp_limit', 'rsvp_count')
    list_filter = ('location','category','date')  # filter model using location, category or date
    search_fields = ('title',)  # search any specific event using event name
    ordering = ['date'] # Newly added  events will show above all events
    sortable_by = ( 'date', 'time') # can sort model based on date and time
# End of addition of code
# Reason - to register event model in admin panel      

# Addition of code
# Reason - to register category model in admin panel      
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')
# End of addition of code
# Reason - to register category model in admin panel          
    
# Addition of code
# Reason - to register RSVP model in admin panel          
@admin.register(RSVP)
class RSVPAdmin(admin.ModelAdmin):
    list_display = ('id','user', 'event', 'created_at')
# Addition of code
# Reason - to register RSVP model in admin panel          
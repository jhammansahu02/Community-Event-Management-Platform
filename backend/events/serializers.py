from rest_framework import serializers
from .models import *

# Addition of code
# REason - added serializer for user model while signup
class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}
# End of addition of code
# REason - added serializer for user model while signup        

# Addition of code
# REASON - added serializer for category model        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'        
# End of addition of code
# Reason - added serializer for category model         
 
# Addition of code
# Reason - added serializer for event model   
class EventSerializer(serializers.ModelSerializer):
    # organizer = LoginSerializer(read_only=True)
    # category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'location', 'organizer', 'category', 'rsvp_limit']
# End of addition of code
# Reason - added serializer for event model     

# Addition of code
# Reason - added serializer for event model   
class EventSerializerForGet(serializers.ModelSerializer):
    organizer = SignupSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    
    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'time', 'location', 'organizer', 'category', 'rsvp_limit']
# End of addition of code
# Reason - added serializer for event model       

# Addition of code
# Reason - added serializer for RSVP model          
class RSVPSerializer(serializers.ModelSerializer):
    class Meta:
        model = RSVP
        fields = ['id', 'user','event','created_at']  
# End of addition of code
# Reason - added serializer for RSVP model                
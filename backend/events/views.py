from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from .serializers import *
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
import jwt
from django.conf import settings
from datetime import datetime

# Addition
# Reason - Added API to handle signup requests
class SignupAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        
        data = {
            "username": request.data["email"],
            "email": request.data["email"].lower(),
            "password": make_password(request.data["password"]),
            "contact_number": request.data["contact_number"],
            "gender": request.data["gender"],
            "first_name": request.data["first_name"],
            "last_name": request.data["last_name"],
        }
        
        userSerializer = SignupSerializer(data=data)

        try:
            if userSerializer.is_valid(raise_exception=True):
                userSerializer.save()
                return Response({
                    "success": "Registration done successfully",
                    "username": userSerializer.data['username']},
                200)
        except Exception as e:
            if "email" in userSerializer.errors.keys():
                return Response({"error": "Email already registered"}, 500)
            return Response(userSerializer.errors, 500)
# End of addition
# Reason - Added API to handle signup requests        
        
# Addition
# Reason - Added API to handle login requests        
class LoginAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data["username"]
        email = email.lower()
        password = request.data["password"]
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                refresh = RefreshToken.for_user(user)

                return Response({
                    'success': 'Login successful',
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                    'user': {"id": user.id,
                             "first_name": user.first_name,
                             "last_name": user.last_name,
                             "email": user.email}
                }, 200)
            else:
                return Response({"error": "Invalid username or password"}, 401)
        except Exception as e:
            return Response({"error": "User not found"}, 404) 
# End of addition of code
# Reason - Added API to handle login request               

# Addition of code
# Reason - Added API to create category for event        
class CategoryAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = {
            "name": request.data['name'],
            "description": request.data['description'],
        }
        
        categorySerializer = CategorySerializer(data = data)
            
        try:
            if categorySerializer.is_valid(raise_exception=True):
                categorySerializer.save()
                return Response({"success": "Category created"}, 200)
        except Exception as e:
           return Response(categorySerializer.errors, 500)
# End of addition of code
# Reason - Added API to create category for event    

# Addition of code
# Reason - Added API to create, delete or update an event   
class EventsCreateDeleteUpdateAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            data = {
                "title": request.data.get('title'),
                "description": request.data.get('description'),
                "location": request.data.get('location'),
                "category": request.data.get('category'),
                "organizer": request.user.id,
                "rsvp_limit": request.data.get('rsvp_limit'),
            }
        
            eventSerializer = EventSerializer(data=data)
            if eventSerializer.is_valid(raise_exception=True):
                eventSerializer.save()
                return Response({"success": "Event created"}, status=200)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            if event.organizer != request.user:
                return Response({"error": "You do not have permission to delete this event"}, 403)
            
            event.delete()
            return Response({"success": "Event deleted"}, status=200)
        
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, 404)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
        
    def patch(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            if event.organizer != request.user:
                return Response({"error": "You do not have permission to edit this event"}, status=status.HTTP_403_FORBIDDEN)
            
            eventSerializer = EventSerializer(event, data=request.data, partial=True)
            if eventSerializer.is_valid(raise_exception=True):
                eventSerializer.save()
                return Response({"success": "Event updated"}, status=200)
        
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=500)    
# End of addition of code
# Reason - Added API to create, delete or update an event    

# Addition of code
# Reason - Added API to fetch one or all event    
class EventListAPI(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request, event_id=None):
        try:
            if event_id:
                events = Event.objects.get(id = event_id)
                serializer = EventSerializerForGet(events)
            else:
                events = Event.objects.all()
                serializer = EventSerializerForGet(events, many=True)
            return Response(serializer.data)    
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=404)
        except Exception as e:
            return Response({"error": "Unable to retrieve events"}, status=500)
        
# End of addition of code
# Reason - Added API to fetch one or all event         
        
# Addition of code
# Reason - Added API to make user respond to events        
class RSVPAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
    
            if RSVP.objects.filter(user=request.user, event=event).exists():
                return Response("An RSVP with this user and event already exists.")
        
            rsvp_count = RSVP.objects.filter(event=event).count()
            if event.rsvp_limit <= rsvp_count:
                return Response({"error": "Event is full"}, 403)
            
            data = {
                "user": request.user.id,
                "event": event_id
            }
            
            rsvpSerializer = RSVPSerializer(data=data)
            if rsvpSerializer.is_valid(raise_exception=True):
                rsvpSerializer.save()
                if event.rsvp_count is None:
                    event.rsvp_count = 1
                else:
                    event.rsvp_count += 1
                return Response({"success": "RSVP successful"}, status=200)
        
        except Event.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
# End of addition of code
# Reason - Added API to make user respond to events                
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('',  HomeView.as_view(),),
    path('admin/', admin.site.urls),
    path('api/v1/', include('events.urls'))
]

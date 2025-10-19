from django.contrib import admin
from django.urls import path, include

from . views import about, home, properties
urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('properties/', properties, name='properties')
]

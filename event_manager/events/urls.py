""" 
EVENT URLs
"""
from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    # events/first
    path("first", views.first_view, name="first_view"),
]

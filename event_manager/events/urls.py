""" 
EVENT URLs
"""
from django.urls import path
from . import views

app_name = "events"

urlpatterns = [

    path("event/create", views.EventCreateView.as_view(), name="event_create"),
    path("event/<int:pk>/update", views.EventUpdateView.as_view(), name="event_update"),
    path("event/<int:pk>/delete", views.EventDeleteView.as_view(), name="event_delete"),
    
    # events (overview list of all events)
    path("", views.EventListView.as_view(), name="events"),

    # events/event/34
    path("event/<int:pk>", views.EventDetailView.as_view(), name="event_detail"),

    # events/categories (list of all Categories)
    path("categories", views.categories, name="categories"),
    path("category/<int:pk>", 
         views.category_detail, 
         name="category_detail"),
    
    # events/category/create GET or POST
    path("category/create", 
         views.category_create, 
         name="category_create"),

     # events/first
    path("first", views.first_view, name="first_view"),
]

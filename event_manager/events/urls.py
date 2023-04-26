""" 
EVENT URLs
"""
from django.urls import path
from . import views

app_name = "events"

urlpatterns = [
    # events/first
    path("first", views.first_view, name="first_view"),

    # events/categories (list of all Categories)
    path("categories", views.categories, name="categories"),
    path("category/<int:pk>", 
         views.category_detail, 
         name="category_detail"),
    
    # events/category/create GET or POST
    path("category/create", 
         views.category_create, 
         name="category_create"),
]

"""
PROJECT URLs
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # events/
    path('events/', include("events.urls")),
]

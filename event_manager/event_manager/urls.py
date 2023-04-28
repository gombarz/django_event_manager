"""
PROJECT URLs
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from drf_spectacular.views import (SpectacularAPIView, 
                                   SpectacularSwaggerView)

from rest_framework.authtoken.views import obtain_auth_token
from events.api.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),

    # events/
    path('events/', include("events.urls")),
    path("", include("pages.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api/events/', include(router.urls)),  # better to events/

    # cccc80546c306826f41c32d46fbcdcf7116edf8b
    path('token', obtain_auth_token, name="api-token"),
    
    # API Schema
    path('schema/', 
         SpectacularAPIView.as_view(api_version="v1"), 
         name="schema"),

    # SWAGGER UI   
    path('api/docs/', 
         SpectacularSwaggerView.as_view(url_name="schema"),
         name="swagger-ui"),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
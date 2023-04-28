from rest_framework import routers

from . import views

router = routers.DefaultRouter()
# api/category
router.register("category", views.CategoryViewSet)

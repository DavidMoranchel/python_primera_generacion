from django.urls import path, include
from rest_framework import routers
from .views import OwnersViewSet

router = routers.DefaultRouter()
router.register(r"owners", OwnersViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
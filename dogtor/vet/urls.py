from django.urls import path

from .views import list_pet_owners

urlpatterns = [path("owners/", list_pet_owners)]

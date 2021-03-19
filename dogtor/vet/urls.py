from django.urls import path

from .views import OwnersList, OwnersDetail, PetsList, PetsDetail

urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnersDetail.as_view(), name="owners_detail"),
    path("pets/", PetsList.as_view(), name="pets_list"),
    path("pets/<int:pk>/", PetsDetail.as_view(), name="pets_detail"),
]

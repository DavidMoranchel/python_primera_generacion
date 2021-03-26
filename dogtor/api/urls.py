from django.urls import path, include

from .views import (
    ListOwnersAPIView,
    RetrieveOwnersAPIView,
    CreateOwnersAPIView,
    UpdateOwnersAPIView,
    DestroyOwnersAPIView,
    RetrieveOwnerPetsAPIView,
    ListPetsAPIView,
    RetrievePetsOwnerAPIView,
)

urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(), name="list-owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve-owners"),
    path(
        "owners/<int:pk>/update/", UpdateOwnersAPIView.as_view(), name="update-owners"
    ),
    path(
        "owners/<int:pk>/destroy/",
        DestroyOwnersAPIView.as_view(),
        name="destroy-owners",
    ),
    path(
        "owners/<int:pk>/pets/",
        RetrieveOwnerPetsAPIView.as_view(),
        name="retrieve-owner-pets",
    ),
    path("pets/", ListPetsAPIView.as_view(), name="list-pets"),
    path(
        "pets/<int:pk>/", RetrievePetsOwnerAPIView.as_view(), name="retrieve-pets-owner"
    ),
]
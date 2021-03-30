from django.urls import path, include
from rest_framework.authtoken import views
from .views import (
    # Owners
    ListOwnersAPIView,
    RetrieveOwnersAPIView,
    CreateOwnersAPIView,
    UpdateOwnersAPIView,
    DestroyOwnersAPIView,
    RetrieveOwnerPetsAPIView,
    # Pets
    ListPetsAPIView,
    RetrievePetsOwnerAPIView,
    RetrieveUpdatePetsAPIView,
    # Users
    CreateUsersAPIView,
)

urlpatterns = [
    # Users
    path("users/create/", CreateUsersAPIView.as_view(), name="create-users"),
    path("users/login/", views.obtain_auth_token, name="login-users"),
    # Owners
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
    # Pets
    path("pets/", ListPetsAPIView.as_view(), name="list-pets"),
    path(
        "pets/<int:pk>/", RetrievePetsOwnerAPIView.as_view(), name="retrieve-pets-owner"
    ),
    path(
        "pets/<int:pk>/retrieve-update/",
        RetrieveUpdatePetsAPIView.as_view(),
        name="retrieve-update-pets",
    ),
]
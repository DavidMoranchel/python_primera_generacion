from rest_framework import generics

from django.contrib.auth.models import User

from vet.models import PetOwner, Pet, PetDate

from .serializers import (
    # Owners
    OwnersListSerializer,
    OwnersSerializer,
    OwnerPetsSerializer,
    # Pets
    PetsListSerializer,
    PetOwnerSerializer,
    PetsSerializer,
    # Users
    UsersSerializer,
)


# Pet Owners
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters


class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer
    # permission_classes = []
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ["first_name", "pets__name"]

    # filter_backends = [filters.SearchFilter]
    # search_fields = ["first_name"]


class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer


class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("type")
    serializer_class = PetsListSerializer


class RetrievePetsOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer


class RetrieveUpdatePetsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


# Users

from rest_framework import permissions


class CreateUsersAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    # permission_classes = []

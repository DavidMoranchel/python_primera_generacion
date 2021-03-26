from rest_framework import generics

from vet.models import PetOwner, Pet, PetDate

from .serializers import OwnersListSerializer, OwnersSerializer

# Create your views here.


class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer


class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

from rest_framework import viewsets

from vet.models import PetOwner
from .serializers import OwnersSerializer

# Create your views here.
class OwnersViewSet(viewsets.ModelViewSet):
    """
    ViewSet del modelo PetOwners.
    """

    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer

from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate

# Serializers define the API representation.


class OwnersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"

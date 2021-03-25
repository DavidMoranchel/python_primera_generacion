from rest_framework import serializers

from vet.models import PetOwner

# Serializers define the API representation.
class OwnersSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "email",
            "phone",
            "address",
            "created_at",
        ]

from rest_framework import serializers
from django.contrib.auth.models import User
from vet.models import PetOwner, Pet, PetDate


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "name"]


class OwnersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = ["id", "first_name", "last_name"]


class PetOwnerSerializer(serializers.ModelSerializer):

    owner = OwnersListSerializer()

    class Meta:
        model = Pet
        fields = ["id", "name", "type", "created_at", "owner"]


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"


class OwnerPetsSerializer(serializers.ModelSerializer):

    pets = PetsListSerializer(many=True)

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
            "pets",
        ]


# Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validate_data):
        print(validate_data)
        user = User.objects.create_user(**validate_data)

        return user
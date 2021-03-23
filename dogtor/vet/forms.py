from django import forms

from .models import PetOwner


class OwnerForm(forms.ModelForm):
    class Meta:
        model = PetOwner
        fields = ["first_name", "last_name", "address", "email", "phone"]
        widgets = {
            "first_name": forms.TextInput(
                attrs={"placeholder": "Pon tu nombre", "class": "clase-custom"}
            )
        }

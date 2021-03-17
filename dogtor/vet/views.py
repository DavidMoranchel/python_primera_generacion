from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import PetOwner

# Create your views here.
def list_pet_owners(request):
    """List owners."""
    owners = PetOwner.objects.all()
    context = {"owners": owners}

    template = loader.get_template("vet/owners/list.html")
    return HttpResponse(template.render(context, request))

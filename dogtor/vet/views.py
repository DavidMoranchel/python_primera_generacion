from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from .forms import OwnerForm

# Create your views here.
class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


class OwnersCreate(CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")


class PetsList(ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"


class PetsDetail(DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"


class PetsCreate(CreateView):
    model = Pet
    template_name = "vet/pets/create.html"
    fields = ["name", "type", "owner"]
    success_url = reverse_lazy("vet:pets_list")
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, ListView, DetailView

from .models import PetOwner

# Create your views here.
class Owners(View):
    def get(self, request):
        owners = PetOwner.objects.all()
        context = {"owners": owners}

        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))


# class OwnersList(TemplateView):
#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context, "ESTO VIENE DEL PADRE (TEMPLATEVIEW)")
#         context["owners"] = PetOwner.objects.all()
#         print(context, "ESTO LE AGREGAMOS NOSOTROS")
#         return context


class OwnersList(ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


class Test(View):
    def get(self, request):
        return HttpResponse("Hello world from class view!!")

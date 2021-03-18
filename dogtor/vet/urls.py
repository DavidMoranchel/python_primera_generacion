from django.urls import path

from .views import Owners, Test

urlpatterns = [path("owners/", Owners.as_view()), path("test/", Test.as_view())]

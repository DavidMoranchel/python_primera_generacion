from django.urls import path

from .views import OwnersList, OwnersDetail

urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/<int:pk>/", OwnersDetail.as_view(), name="owners_detail"),
]

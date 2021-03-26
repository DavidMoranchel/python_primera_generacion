from django.urls import path, include

from .views import ListOwnersAPIView, RetrieveOwnersAPIView, CreateOwnersAPIView

urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(), name="list-owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve-owners"),
]
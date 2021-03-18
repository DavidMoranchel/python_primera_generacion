from django.urls import path

from .views import Owners, Test, OwnersList, OwnersDetail

urlpatterns = [
    path("owners/", OwnersList.as_view()),
    path("owners/<int:pk>/", OwnersDetail.as_view()),
    path("test/", Test.as_view()),
]

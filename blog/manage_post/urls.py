from django.urls import path

from . import views

urlpatterns = [
    path("", views.ShowIndex, name="index"),
]
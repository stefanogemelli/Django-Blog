from django.urls import path

from . import views

urlpatterns = [
    path("/", views.ShowIndex, name="index"),
    path("/edit", views.EditUser, name="edit_user"),
    path("/login", views.EditUser, name="login"),
    path("/logout", views.EditUser, name="logout"),
]
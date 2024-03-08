from django.urls import path

from user import views

urlpatterns = [
    path("add/", views.SignUpView.as_view(), name="register"),
]
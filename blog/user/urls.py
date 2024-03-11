from django.urls import path
from user import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("add/", views.SignUpView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),

    #provisional para que no rompa el template
    path("passwordreset/", views.LoginView.as_view(), name="password_reset"),
    path("edit/", views.LoginView.as_view(), name="edit_user"),
]
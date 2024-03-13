from django.urls import path
from user import views

urlpatterns = [
    path("add/", views.SignUpView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("edit/", views.UserUpdateView.as_view(), name="edit_user"),
    path("delete/", views.UserDeleteView.as_view(), name="delete_user"),
    path("password/", views.PasswordsChangeView.as_view(), name="change_password"),

    #provisional para que no rompa el template
    path("passwordreset/", views.LoginView.as_view(), name="password_reset"),
]
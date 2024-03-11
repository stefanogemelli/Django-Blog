from django.views.generic import CreateView
from user.forms import SignUpForm, LoginForm
from django.contrib.auth.views import LoginView


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "login/register.html"

class LoginView(LoginView):
    form_class = LoginForm
    template_name = "login/login.html"
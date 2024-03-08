from django.http import HttpResponse
from django.views.generic import CreateView
from user.forms import SignUpForm


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "login/register.html"


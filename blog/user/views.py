from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from user.forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect

from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect("login")


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = "login/register.html"

    def form_valid(self, form):
        #Si es válido, guardar
        form.save()

        #Obtener username y password
        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )

        #Solicitud de inicio de sesión
        login(self.request, user)
        return redirect("index")


class LoginView(LoginView):
    form_class = LoginForm
    template_name = "login/login.html"
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


class SignUpForm(UserCreationForm):
    username = forms.CharField(label=False,widget=forms.TextInput(attrs={"placeholder":"Nombre de usuario"}) )
    full_name = forms.CharField(label=False,widget=forms.TextInput(attrs={"placeholder":"Nombre completo"}) )
    email = forms.CharField(label=False,widget=forms.TextInput(attrs={"placeholder":"Email"}) )
    password1 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={"placeholder":"Contraseña"}) )
    password2 = forms.CharField(label=False,widget=forms.PasswordInput(attrs={"placeholder":"Confirmar contraseña"}) )

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "email",
            "password1",
            "password2"
        ]
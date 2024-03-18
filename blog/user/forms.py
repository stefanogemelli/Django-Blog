from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.contrib.auth import get_user_model
User = get_user_model()
from user.models import Profile


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

class LoginForm(AuthenticationForm):
    username = forms.CharField(label=False, help_text=None,widget=forms.TextInput(attrs={"placeholder":"Nombre de usuario"}))
    password = forms.CharField(label=False, help_text=None,widget=forms.PasswordInput(attrs={"placeholder":"Contraseña"}))
    class Meta:
        model = User
        fields = [
            "username",
            "password"
        ]

class UserForm(forms.ModelForm):

    username = forms.CharField(help_text=None,
                               label="Nombre de usuario")
    
    full_name = forms.CharField(help_text=None,
                                label="Nombre completo")
    email = forms.EmailField(label="Correo")

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "email",
        ]

class ProfileForm(forms.ModelForm):
    photo = forms.ImageField(label="Foto",
                             help_text=None,
                             required=False,
                             widget=forms.FileInput())
    profession = forms.CharField(required=False)
    about = forms.CharField(required=False)
    birthday = forms.DateField(required=False,widget=forms.SelectDateWidget(years=range(1940,2024)))
    twitter = forms.CharField(required=False)
    linkedin = forms.CharField(required=False)
    facebook = forms.CharField(required=False)
    
    class Meta:
        model = Profile
        fields = [
            "photo",
            "profession",
            "about",
            "birthday",
            "twitter",
            "linkedin",
            "facebook",
        ]

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={"placeholder":"Antigua contraseña"}))
    
    new_password1 = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={"placeholder":"Nueva contraseña"}))
    
    new_password2 = forms.CharField(label=False,
                                   widget=forms.PasswordInput(attrs={"placeholder":"Confirmar contraseña"}))
    class Meta:
        model = User
        fields = [
            "old_password",
            "new_passowrd1",
            "new_password2",
        ]
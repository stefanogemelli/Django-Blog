from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, DeleteView
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from user.forms import ProfileForm, SignUpForm, LoginForm, UserForm, PasswordChangingForm
from user.models import Profile
from django.contrib.auth import get_user_model
User = get_user_model()
from django.views.generic import CreateView, TemplateView, DetailView
from manage_post.models import Article


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

class UserUpdateView(LoginRequiredMixin, TemplateView):
    login_url = "login"
    user_form = UserForm
    profile_form = ProfileForm

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data,file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            #Aplicar cambios
            user_form.save()
            profile_form.save()
            
            return redirect("index")
    
        #Enviar los formularios como contexto
        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )
        return render(request,"profile/edit_profile.html", context)
    
    def get(self, request, *args, **kwargs):
        if Profile.objects.filter(user=request.user).exists() == False:
            Profile.objects.create(user=request.user)
        return self.post(request, *args, **kwargs)

class UserDeleteView(DeleteView):
    model = User
    template_name = "profile/delete_user.html"
    success_url = reverse_lazy("index")

    def get_object(self, queryset=None):
        return User.objects.get(id=self.request.user.id)
    
class PasswordsChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url = "login"
    template_name = "password/change_password.html"
    form_class = PasswordChangingForm
    success_url = reverse_lazy("index")

class ViewProfile(DetailView):
    model = User
    template_name = "profile/view_profile.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["posts"] = Article.objects.filter(user_id=User.objects.get(id=self.kwargs["pk"]))
        return context


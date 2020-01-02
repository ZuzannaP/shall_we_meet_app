from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

from .models import CustomUser
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm


def homepage(request):
    return render(request, "homepage.html")

### USER ADMINISTRATION ###


class LoginView(FormView):
    form_class = LoginForm
    success_url = "/"
    template_name = "login.html"

    def form_valid(self, form: LoginForm):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(self.request, username=username, password=password)

        if user is None:
            form.add_error(None, "Incorrect login or password")
            return super().form_invalid(form)

        login(self.request, user)
        return super().form_valid(form)


class LogoutView(View):
    def get(self, request):
        return render(request, "logout.html")

    def post(self, request):
        ctx = {}
        logout(request)
        if request.user.is_authenticated:
            ctx["my_verdict"] = "Ups. Something went wrong."
        else:
            ctx["my_verdict"] = "You have been logged out"
        return render(request, "logout.html", ctx)


# dodaj powitalny message
class SignUpView(SuccessMessageMixin, CreateView,):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    success_message = 'Your account has been created. Welcome on board!'
    template_name = 'signup.html'


class EditPersonalInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('homepage')
    success_message = "Your personal data has been succesfully changed!"
    template_name = 'edit_personal_info.html'

    def get_object(self):
        return self.request.user


# dodaj message , że konto zostało skasowane
class DeleteAccountView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'account_confirm_delete.html'
    model = CustomUser
    success_url = reverse_lazy("homepage")
    success_message = "Your account has been deleted"

    def get_object(self):
        return self.request.user


class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'password_change.html'


class CustomPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    template_name = 'password_change_done.html'

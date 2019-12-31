from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView

from .models import CustomUser
from .forms import LoginForm, CustomUserCreationForm


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
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

#trzeba być zalogowanym, by móc to zrobić i tylko można się do swojego numerka dostać!
#dodaj message, że zmiany zostały zapisane
class EditPersonalInfoView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ( 'first_name', 'last_name', 'email', 'street', 'house_nr', 'zip_code', 'city')
    success_url = reverse_lazy('homepage')
    template_name = 'edit_personal_info.html'

#dodaj message , że konto zostało skasowane
class DeleteAccountView(LoginRequiredMixin, DeleteView):
    template_name = 'account_confirm_delete.html'
    model = CustomUser
    success_url = reverse_lazy("homepage")
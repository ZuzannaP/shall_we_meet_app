from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from .models import CustomUser, Event
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm, CreateEventForm


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


class AccountSettingsView(View):
    def get(self, request):
        return render(request, "account_settings_tmp.html")


class SignUpView(SuccessMessageMixin, CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    success_message = 'Your account has been created. Welcome on board!'
    template_name = 'signup.html'


class EditPersonalInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("homepage")
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


## EVENT ADMINISTRATION ##


class CreateEventView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    def get(self, request):
        form = CreateEventForm()
        ctx = {"form": form}
        return render(request, "create_event_tmp.html", ctx)

    def post(self, request):
        form = CreateEventForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            description = form.cleaned_data["description"]
            location = form.cleaned_data["location"]
            approx_duration = form.cleaned_data["approx_duration"]
            participants = form.cleaned_data["participants"]
            event = Event.objects.create(title=title, description=description, location=location,
                                         approx_duration=approx_duration, owner=request.user)
            for participant in participants:
                event.participants.add(participant)
            messages.success(request, 'Event has been created!')
            return redirect(f'/event/view/{event.id}/')
        ctx = {"form": form}
        return render(request, "create_event_tmp.html", ctx)


class EventView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = "view_event_tmp.html"


class EditEventView(LoginRequiredMixin, SuccessMessageMixin, View):
    pass


class DeleteEventView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    pass


class OrganizerInProgressView(LoginRequiredMixin, View):

    def get(self, request):
        events = Event.objects.all().filter(owner=self.request.user).filter(is_in_progress=True)
        return render(request, "owner_in_progress_tmp.html",{"events":events})


class OrganizerUpcomingView(LoginRequiredMixin, ListView):
    def get(self, request):
        events = Event.objects.all().filter(owner=self.request.user).filter(is_upcoming=True)
        return render(request, "owner_upcoming_tmp.html", {"events": events})


class OrganizerArchiveView(LoginRequiredMixin, ListView):
    def get(self, request):
        events = Event.objects.all().filter(owner=self.request.user).filter(is_archive=True)
        return render(request, "owner_archive_tmp.html", {"events": events})



from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import CreateView, FormView, UpdateView, DeleteView
from .models import CustomUser, Event, DateTimeSlot, ParticipantSlotVote
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm, CreateEventForm, \
    EditEventForm, CustomDatetimePicker


def homepage(request):
    ctx = {}
    if request.user.is_authenticated:
        ctx["events"] = Event.objects.filter(Q(owner=request.user) | Q(participants=request.user)).filter(Q(is_in_progress=True) | Q(is_upcoming=True)).distinct()
        return render(request, "homepage.html", ctx)
    else:
        ctx["events"] = "n/a"
        return render(request, "homepage.html", ctx)


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


class CreateEventView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreateEventForm(excluding_owner=request.user)
        ctx = {"form": form}
        return render(request, "create_event_tmp.html", ctx)

    def post(self, request):
        form = CreateEventForm(request.POST, excluding_owner=request.user)
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
            return redirect(f'/event/create/timeslots/{event.id}/')
        ctx = {"form": form}
        return render(request, "create_event_tmp.html", ctx)


class ProposeTimeslotsView(LoginRequiredMixin, View):
    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        timeslots_nr = event.event_datetimeslot.count()
        print(timeslots_nr)
        form = CustomDatetimePicker(instance=event)
        ctx = {"form": form, "event": event, "timeslots_nr":timeslots_nr}
        return render(request, "propose_time_slots_tmp.html", ctx)

    def post(self, request, event_id):
        form = CustomDatetimePicker(request.POST)
        if form.is_valid():
            date_time_from = form.cleaned_data["date_time_from"]
            date_time_to = form.cleaned_data["date_time_to"]
            event = Event.objects.get(pk=event_id)
            datetimeslot = DateTimeSlot.objects.create(date_time_from=date_time_from, date_time_to=date_time_to, event=event)
            event_participants = event.participants.all()
            for participant in event_participants:
                datetimeslot.participants.add(participant)
            messages.success(request, f'Timeslot from {date_time_from.strftime("%d.%m.%Y at %H:%M:%S")} to {date_time_to.strftime("%d.%m.%Y at %H:%M:%S")} has been added!')
            return redirect(f'/event/create/timeslots/{event.id}/')
        ctx = {"form": form}
        return render(request, "propose_time_slots_tmp.html", ctx)


class EventView(LoginRequiredMixin, View):

#TODO: jak to podzielić na 2 funkcje, bo za dużo tu kontentu na jedna?

    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        participants_nr = event.participants.count()
        event_votes = {}
        tuples_yes = []
        tuples_no = []
        tuples_if_need_be = []
    # extracting each vote
        for slot in event.event_datetimeslot.all():
            slot_votes = {"yes": 0, "no": 0, "if_need_be": 0}
            for datetime in slot.participants_votes.all():
                if datetime.vote == 1:
                    slot_votes["no"] += 1
                elif datetime.vote == 2:
                    slot_votes["yes"] += 1
                elif datetime.vote == 3:
                    slot_votes["if_need_be"] += 1
            event_votes[slot] = slot_votes
    # counting the winning datetime slot
            tuples_yes.append((slot_votes["yes"], slot),)
            tuples_no.append((slot_votes["no"], slot),)
            tuples_if_need_be.append((slot_votes["if_need_be"], slot),)
            highest_yes = max(tuples_yes, key=lambda item: item[0])
            highest_no = max(tuples_no, key=lambda item: item[0])
            highest_if_need_be = max(tuples_if_need_be, key=lambda item: item[0])
        ctx = {"event": event, "event_votes": event_votes, "winning" : highest_yes[1]}
        return render(request, "view_event_tmp.html", ctx)


#TODO: na razie robocze edytowanie. Potem ustalę ostatecznie co można zmieniać, czego nie
# poza tym zrób tak jak w create view, żeby ownera nie wyśwwietlało jako możliwego partycypanta
class EditEventView(LoginRequiredMixin,  UpdateView):
    model = Event
    form_class = EditEventForm
    template_name = "edit_event_tmp.html"

    def get_success_url(self):
        event_id = self.kwargs['pk']
        return reverse_lazy('edit_timeslots', kwargs={'pk': event_id})


#TODO: dodaj opcję edycji oraz opcję usunięcia pojedynczego datetimeslotu i dodania timeslotu (do  pierwszego wystarczy zmienić link na guzik, do drugiego trzeba stworzyć nowy deleteview
class EditTimeslotsView(LoginRequiredMixin,  ListView):
    def get(self, request, pk):
        event = Event.objects.get(pk=pk)
        timeslots = event.event_datetimeslot.all()
        return render(request, "edit_time_slots_tmp.html", {"timeslots": timeslots, "event":event})

# todo chyba do usunięcia, bo nie chcę jednak dawać możliwości edycji timeslots, jak już ktoś zagłosował - można zmienić tylko jak nikt nie zagłosował!
class EditOneTimeslotView(LoginRequiredMixin,  UpdateView):
    model = DateTimeSlot
    form_class = CustomDatetimePicker
    template_name = "edit_one_time_slot_tmp.html"

    def get_success_url(self):
        datetime_id = self.kwargs['pk']
        datetime = DateTimeSlot.objects.get(pk=datetime_id)
        event_id = datetime.event.pk
        return reverse_lazy('edit_timeslots', kwargs={'pk': event_id})


class DeleteEventView(LoginRequiredMixin, View):
    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        return render(request, "delete_event_tmp.html", {"event": event})

    def post(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        try:
            event.delete()
            messages.success(request, 'Event has been succesfully deleted')
            return render(request, "homepage.html")
        except Exception as e:
            messages.ERROR(request, "There was a problem while deleting. Try again.")
            return render(request, "delete_event_tmp.html", {"event": event})


class OrganizerInProgressView(LoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.filter(owner=self.request.user).filter(is_in_progress=True)
        return render(request, "owner_in_progress_tmp.html",{"events":events})


class OrganizerUpcomingView(LoginRequiredMixin, ListView):
    def get(self, request):
        events = Event.objects.filter(owner=self.request.user).filter(is_upcoming=True)
        return render(request, "owner_upcoming_tmp.html", {"events": events})


class OrganizerArchiveView(LoginRequiredMixin, ListView):
    def get(self, request):
        events = Event.objects.filter(owner=self.request.user).filter(is_archive=True)
        return render(request, "owner_archive_tmp.html", {"events": events})


class AsGuestInProgressView(LoginRequiredMixin, View):
    def get(self, request):
        events = Event.objects.filter(participants=request.user).filter(is_in_progress=True)
        event_votes = {}
        for event in events:
            timeslots = event.event_datetimeslot.all()
            event_votes[event] = "ok"
            for slot in timeslots:
                my_vote = ParticipantSlotVote.objects.filter(participant=request.user).filter(slot=slot)[0]
                if my_vote.vote == -2:
                    event_votes[event] = "missing"
        return render(request, "guest_in_progress_tmp.html", { "event_votes": event_votes})


class AsGuestUpcomingView(LoginRequiredMixin, ListView):
    def get(self, request):
        events = Event.objects.filter(participants=request.user).filter(is_upcoming=True)
        return render(request, "guest_upcoming_tmp.html", {"events": events})


class AsGuestArchiveView(LoginRequiredMixin, ListView):
    def get(self, request):
        events = Event.objects.filter(participants=request.user).filter(is_archive=True)
        return render(request, "guest_archive_tmp.html", {"events": events})


class VoteForTimeslotsView(LoginRequiredMixin, View):
    def get(self, request, event_id):
        event = Event.objects.get(pk=event_id)
        timeslots = event.event_datetimeslot.all()
        vote_list = {}
        if request.user in event.participants.all():
            for slot in timeslots:
                my_vote = ParticipantSlotVote.objects.filter(participant=request.user).filter(slot=slot)[0]
                vote_list[slot] = my_vote.vote
            ctx = {"timeslots": timeslots, "event": event, 'vote_list':vote_list}
            return render(request, "vote_for_timeslots_tmp.html", ctx)
        else:
            raise PermissionDenied("You are not authorized!")


class VoteView(LoginRequiredMixin, SuccessMessageMixin, View):
    def get(self, request, timeslot_id, vote):
        timeslot = DateTimeSlot.objects.get(pk=timeslot_id)
        thevote = 2 if vote == "yes" else (1 if vote == "no" else "ifneedbe")
        event = timeslot.event
        participantslotvote = ParticipantSlotVote.objects.filter(participant=request.user, slot=timeslot)[0]
        participantslotvote.vote = thevote
        participantslotvote.save()
        return redirect(f'/event/vote/timeslots/{event.id}')
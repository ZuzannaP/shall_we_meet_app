import json
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView, UpdateView, DeleteView
from .models import CustomUser, Event, DateTimeSlot, ParticipantSlotVote
from .forms import LoginForm, CustomUserCreationForm, CustomUserChangeForm, CreateEventForm, \
    EditEventForm, CustomDatetimePicker, ChooseMeetingLocationForm, EditMeetingLocationForm


def homepage(request):
    ctx = {}
    if request.user.is_authenticated:
        ctx["events"] = Event.objects.filter(Q(owner=request.user) | Q(participants=request.user)).filter(
            Q(is_in_progress=True) | Q(is_upcoming=True)).distinct()
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


class SignUpView(View):

    def get(self, request):
        form = CustomUserCreationForm()
        ctx = {"form": form}
        return render(request, "signup.html", ctx)

    def post(self, request):
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your account has been created!")
            return redirect('login')
        messages.error(request, "Please remember to put a pin where your residency address is!")
        ctx = {"form": form}
        return render(request, "signup.html", ctx)


class EditPersonalInfoView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    form_class = CustomUserChangeForm
    success_url = reverse_lazy("homepage")
    success_message = "Your personal data has been succesfully changed!"
    template_name = 'edit_personal_info.html'

    def get_object(self):
        return self.request.user


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
            participants = form.cleaned_data["participants"]
            event = Event.objects.create(title=title, description=description, owner=request.user)
            for participant in participants:
                event.participants.add(participant)
            return redirect("choose_location", event.id)
        ctx = {"form": form}
        return render(request, "create_event_tmp.html", ctx)


class ChooseMeetingLocationView(LoginRequiredMixin, View):

    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        if event.owner != request.user:
            raise PermissionDenied
        form = ChooseMeetingLocationForm()
        participants_coordinates = [ [participant.geographical_coordinates.coords[1],participant.geographical_coordinates.coords[0]] for participant in event.participants.all()]
        participants_coordinates.append([event.owner.geographical_coordinates.coords[1], event.owner.geographical_coordinates.coords[0]])
        ctx = {"form": form, "participants_coordinates": json.dumps(participants_coordinates)}
        return render(request, "choose_meeting_location_tmp.html", ctx)

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        form = ChooseMeetingLocationForm(request.POST)
        if form.is_valid():
            meeting_address = form.cleaned_data["meeting_address"]
            meeting_geographical_coordinates = form.cleaned_data["meeting_geographical_coordinates"]
            location_comments = form.cleaned_data["location_comments"]
            event.meeting_address = meeting_address
            event.meeting_geographical_coordinates = meeting_geographical_coordinates
            event.location_comments = location_comments
            event.save()
            messages.success(request, "Location saved!")
            return redirect("propose_timeslots", event.id)
        messages.error(request, "Please remember to put a pin on the map!")
        ctx = {"form": form}
        return render(request, "choose_meeting_location_tmp.html", ctx)



class ProposeTimeslotsView(LoginRequiredMixin, View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        if event.owner != request.user:
            raise PermissionDenied
        timeslots_nr = event.event_datetimeslot.count()
        form = CustomDatetimePicker(instance=event)
        ctx = {"form": form, "event": event, "timeslots_nr": timeslots_nr}
        return render(request, "propose_time_slots_tmp.html", ctx)

    def post(self, request, event_id):
        form = CustomDatetimePicker(request.POST)
        if form.is_valid():
            date_time_from = form.cleaned_data["date_time_from"]
            date_time_to = form.cleaned_data["date_time_to"]
            event = get_object_or_404(Event, pk=event_id)
            datetimeslot = DateTimeSlot.objects.create(date_time_from=date_time_from, date_time_to=date_time_to,
                                                       event=event)
            event_participants = event.participants.all()
            for participant in event_participants:
                datetimeslot.participants.add(participant)
            messages.success(request,
                             f'Timeslot from {date_time_from.strftime("%d.%m.%Y at %H:%M:%S")} to {date_time_to.strftime("%d.%m.%Y at %H:%M:%S")} has been added!')
            return redirect("propose_timeslots", event_id)
        ctx = {"form": form}
        return render(request, "propose_time_slots_tmp.html", ctx)


class GenericEventView(View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        if self.template_name == "complete_event_tmp.html":
            if event.owner != request.user:
                raise PermissionDenied
        participants_nr = event.participants.count()
        event_votes = {}
        summary_votes = []
        participants_that_voted = set()
        for slot in event.event_datetimeslot.iterator():
            slot_votes = {"no": slot.participants_votes.filter(vote=1).count(),
                          "yes": slot.participants_votes.filter(vote=2).count(),
                          "if_need_be": slot.participants_votes.filter(vote=3).count()}
            participants_that_voted.update(
                list(slot.participants_votes.values_list("participant", flat=True).exclude(vote=-2)))
            score = (((slot_votes["yes"] * 1) + (slot_votes["if_need_be"] * 0.5)) / participants_nr) * 100
            summary_votes.append((score, slot,))
            event_votes[slot] = slot_votes
        if summary_votes:
            highest = max(summary_votes, key=lambda item: item[0])
            winnings = [vote[1] for vote in summary_votes if vote[0] == highest[0] and highest[0] > 0]
        else:
            winnings = None
        participants_pct = int((len(participants_that_voted) / participants_nr) * 100)
        chosen_slot = event.event_datetimeslot.filter(winning=True).first()
        if event.meeting_geographical_coordinates:
            geographical_coordinates = json.dumps([event.meeting_geographical_coordinates.coords[1], event.meeting_geographical_coordinates.coords[0]])
        else:
            geographical_coordinates = json.dumps(None)
        ctx = self.get_context(request, event, event_votes, winnings, participants_pct, chosen_slot, geographical_coordinates)
        return render(request, self.template_name, ctx)


class EventView(LoginRequiredMixin, GenericEventView):
    template_name = "view_event_tmp.html"

    def get_context(self, request, event, event_votes, winning, participants_pct, chosen_slot, geographical_coordinates):
        return {"event": event, "event_votes": event_votes, "winning": winning, "participants_pct": participants_pct,
                "chosen_slot": chosen_slot, "geographical_coordinates":geographical_coordinates}


class CompleteEventView(LoginRequiredMixin, SuccessMessageMixin, GenericEventView):
    template_name = "complete_event_tmp.html"

    def get_context(self, request, event, event_votes, winning, participants_pct, chosen_slot, geographical_coordinates):
        return {"event": event, "event_votes": event_votes, "winning": winning, "participants_pct": participants_pct,
                "chosen_slot": chosen_slot, "geographical_coordinates":geographical_coordinates}

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        selected_choice = request.POST.get("chosen_slot")
        chosen_slot = DateTimeSlot.objects.get(pk=selected_choice)
        all_slots = event.event_datetimeslot.all()
        for slot in all_slots:
            slot.winning = False
            slot.save()
        chosen_slot.winning = True
        chosen_slot.save()
        event.is_in_progress = False
        event.is_upcoming = True
        event.save()
        return redirect("event_view", event_id)


class EditEventView(LoginRequiredMixin, UpdateView):
    model = Event
    template_name = "edit_event_tmp.html"
    form_class = EditEventForm

    def get_object(self, **kwargs):
        event_object = super().get_object(**kwargs)
        if event_object.owner != self.request.user:
            raise PermissionDenied
        return event_object

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["excluding_owner"] = self.request.user
        return kwargs

    def get_success_url(self):
        event_id = self.kwargs['pk']
        return reverse_lazy('edit_location', kwargs={'pk': event_id})


class EditMeetingLocationView(LoginRequiredMixin, View):

    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if event.owner != request.user:
            raise PermissionDenied
        form = EditMeetingLocationForm(instance=event)
        participants_coordinates = [ [participant.geographical_coordinates.coords[1], participant.geographical_coordinates.coords[0]] for participant in event.participants.all()]
        participants_coordinates.append([event.owner.geographical_coordinates.coords[1], event.owner.geographical_coordinates.coords[0]])
        ctx = {"form": form, "participants_coordinates": json.dumps(participants_coordinates)}
        return render(request, "edit_meeting_location_tmp.html", ctx)

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        form = EditMeetingLocationForm(request.POST)
        if form.is_valid():
            meeting_address = form.cleaned_data["meeting_address"]
            meeting_geographical_coordinates = form.cleaned_data["meeting_geographical_coordinates"]
            location_comments = form.cleaned_data["location_comments"]
            event.meeting_address = meeting_address
            event.meeting_geographical_coordinates = meeting_geographical_coordinates
            event.location_comments = location_comments
            event.save()
            messages.success(request, "Location changed!")
            return redirect("edit_timeslots", event.id)
        messages.error(request, "Please remember to put a pin on the map!")
        ctx = {"form": form}
        return render(request, "edit_meeting_location_tmp.html", ctx)


class EditTimeslotsView(LoginRequiredMixin, ListView):
    def get(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        if event.owner != request.user:
            raise PermissionDenied
        timeslots = event.event_datetimeslot.all()
        return render(request, "edit_time_slots_tmp.html", {"timeslots": timeslots, "event": event})

    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        timeslots = event.event_datetimeslot.all()
        timeslot_id = request.POST.get("timeslot_pk")
        timeslot = DateTimeSlot.objects.get(pk=timeslot_id)
        timeslot.delete()
        return render(request, "edit_time_slots_tmp.html", {"timeslots": timeslots, "event": event})


class EditOneTimeslotView(LoginRequiredMixin, UpdateView):
    model = DateTimeSlot
    form_class = CustomDatetimePicker
    template_name = "edit_one_time_slot_tmp.html"

    def get_object(self, **kwargs):
        event_object = super().get_object(**kwargs)
        if event_object.event.owner != self.request.user:
            raise PermissionDenied
        return event_object

    def get_success_url(self):
        datetime_id = self.kwargs['pk']
        datetime = DateTimeSlot.objects.get(pk=datetime_id)
        event_id = datetime.event.pk
        return reverse_lazy('edit_timeslots', kwargs={'pk': event_id})


class DeleteEventView(LoginRequiredMixin, View):
    def get(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
        if event.owner != request.user:
            raise PermissionDenied
        return render(request, "delete_event_tmp.html", {"event": event})

    def post(self, request, event_id):
        event = get_object_or_404(Event, pk=event_id)
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
        return render(request, "owner_in_progress_tmp.html", {"events": events})


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
        return render(request, "guest_in_progress_tmp.html", {"event_votes": event_votes})


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
        event = get_object_or_404(Event, pk=event_id)
        timeslots = event.event_datetimeslot.all()
        vote_list = {}
        if request.user in event.participants.all():
            for slot in timeslots:
                my_vote = ParticipantSlotVote.objects.filter(participant=request.user).filter(slot=slot)[0]
                vote_list[slot] = my_vote.vote
            ctx = {"timeslots": timeslots, "event": event, 'vote_list': vote_list}
            return render(request, "vote_for_timeslots_tmp.html", ctx)
        else:
            raise PermissionDenied


class VoteView(LoginRequiredMixin, SuccessMessageMixin, View):
    def get(self, request, timeslot_id, vote):
        timeslot = get_object_or_404(DateTimeSlot, pk=timeslot_id)
        thevote = 2 if vote == "yes" else (1 if vote == "no" else 3)
        event = timeslot.event
        participantslotvote = ParticipantSlotVote.objects.filter(participant=request.user, slot=timeslot)[0]
        participantslotvote.vote = thevote
        participantslotvote.save()
        return redirect("vote_for_timeslots", event.id)

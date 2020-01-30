import json
from django.utils.html import escapejs
from django.utils.safestring import mark_safe
from .models import Event, ParticipantSlotVote, CustomUser


def navbar_input(request):
    if request.user.is_authenticated:
        owner_pending_actions = Event.objects.filter(owner=request.user).filter(is_in_progress=True)
        owner_upcoming_events = Event.objects.filter(owner=request.user).filter(is_upcoming=True)
        events = Event.objects.filter(participants=request.user).filter(is_in_progress=True)
        guest_pending_actions = 0
        for event in events:
            timeslots = event.event_datetimeslot.all()
            for slot in timeslots:
                my_vote = ParticipantSlotVote.objects.filter(participant=request.user).filter(slot=slot)[0]
                if my_vote.vote == -2:
                    guest_pending_actions += 1
                    break
        guest_upcoming_events = Event.objects.filter(participants=request.user).filter(is_upcoming=True)
        ctx = {"owner_pending_actions": owner_pending_actions, "owner_upcoming_events": owner_upcoming_events, \
               "guest_pending_actions": guest_pending_actions, "guest_upcoming_events": guest_upcoming_events}
        return ctx
    else:
        ctx = {"owner_pending_actions": "n/a", "owner_upcoming_events":"n/a", "guest_pending_actions": "n/a", "guest_upcoming_events":"n/a"}
        return ctx


# def user_datails(request):
#     user_d = CustomUser.objects.get(pk=3)
#     user_datailing = {'address': [float(coord) for coord in reversed(user_d.geographical_coordinates.coords)]}
#     return {"user_detailing": mark_safe(escapejs(json.dumps(user_datailing)))}
#
#

from django.db.models import Q

from .models import Event, ParticipantSlotVote


def navbar_input(request):
    if request.user.is_authenticated:
        owner_pending_actions = Event.objects.filter(owner=request.user).filter(is_in_progress=True)
        events = Event.objects.filter(participants=request.user).filter(is_in_progress=True)
        guest_pending_actions = 0
        for event in events:
            timeslots = event.event_datetimeslot.all()
            for slot in timeslots:
                my_vote = ParticipantSlotVote.objects.filter(participant=request.user).filter(slot=slot)[0]
                if my_vote.vote == -2:
                    guest_pending_actions += 1
                    break
        ctx = {"owner_pending_actions": owner_pending_actions, "guest_pending_actions": guest_pending_actions}
        return ctx
    else:
        ctx = {"owner_pending_actions": "n/a", "guest_pending_actions": "n/a"}
        return ctx




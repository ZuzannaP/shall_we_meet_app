from django.db.models import Q

from .models import Event, ParticipantSlotVote


def navbar_input(request):
    if request.user.is_authenticated:
        owner_pending_actions = Event.objects.filter(owner=request.user).filter(is_in_progress=True)
        guest_pending_actions = Event.objects.filter(Q(is_in_progress=True) & Q(participants=request.user)).distinct()
        ctx = {"owner_pending_actions": owner_pending_actions, "guest_pending_actions": guest_pending_actions}
        return ctx
    else:
        ctx = {"owner_pending_actions": "n/a", "guest_pending_actions": "n/a"}
        return ctx



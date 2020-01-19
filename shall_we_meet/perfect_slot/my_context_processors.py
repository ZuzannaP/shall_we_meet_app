from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

from .models import Event


def navbar_input(request):
    if request.user.is_authenticated:
        owner_in_progress = Event.objects.all().filter(owner=request.user).filter(is_in_progress=True)
        guest_in_progress = Event.objects.exclude(owner=request.user).filter(is_in_progress=True)
        ctx = {"owner_in_progress": owner_in_progress, "guest_in_progress": guest_in_progress}
        return ctx
    else:
        ctx = {"owner_in_progress": "n/a", "guest_in_progress": "n/a"}
        return ctx


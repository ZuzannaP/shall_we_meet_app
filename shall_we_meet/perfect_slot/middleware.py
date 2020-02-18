from django.utils import timezone
from .models import Event


def archiving_middleware(get_response):
    """Catches events that become overdue - changes their status to is_archive"""

    def middleware(request):
        Event.objects.filter(is_upcoming=True,
                             event_datetimeslot__winning=True,
                             event_datetimeslot__date_time_to__lt=timezone.now()).update(is_upcoming=False,
                                                                                         is_archive=True)
        response = get_response(request)
        return response

    return middleware

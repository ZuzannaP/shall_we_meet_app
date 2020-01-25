from .models import Event
from django.utils import timezone

def archiving_middleware(get_response):

    def middleware(request):
        # upcoming_events = Event.objects.filter(is_upcoming=True)
        # for event in upcoming_events:
        #     chosen_slot = event.event_datetimeslot.filter(winning=True).first()
        #     if chosen_slot and chosen_slot.date_time_to < timezone.now():
        #         event.is_upcoming = False
        #         event.is_archive = True
        #         event.save()

        Event.objects.filter(is_upcoming=True,
                            event_datetimeslot__winning=True,
                            event_datetimeslot__date_time_to__lt = timezone.now()).update(is_upcoming = False, is_archive = True)

        response = get_response(request)
        return response

    return middleware
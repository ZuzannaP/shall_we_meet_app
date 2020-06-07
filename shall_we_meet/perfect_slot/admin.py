from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Event, DateTimeSlot, ParticipantSlotVote


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['username','first_name', 'last_name', 'is_active']

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ([ 'geographical_coordinates'])
    }),
    )

    # unables 'add user' functionality in DjangoAdmin (as it can't be done correctly
    # with current geographical_coordinates logic)
    def has_add_permission(self, request):
        return False



admin.site.register(CustomUser, CustomUserAdmin),
admin.site.register(Event),
admin.site.register(DateTimeSlot),
admin.site.register(ParticipantSlotVote)

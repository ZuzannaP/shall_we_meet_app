from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser, Event, DateTimeSlot, ParticipantSlotVote


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    model = CustomUser
    list_display = ['username', 'is_active', ]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': (['geographical_coordinates'])}),
    )


admin.site.register(CustomUser, CustomUserAdmin),
admin.site.register(Event),
admin.site.register(DateTimeSlot),
admin.site.register(ParticipantSlotVote)

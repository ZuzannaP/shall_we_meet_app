from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    # form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username',]

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('street', 'house_nr', 'zip_code', 'city')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
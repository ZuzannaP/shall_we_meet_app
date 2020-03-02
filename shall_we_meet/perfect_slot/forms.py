from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from tempus_dominus.widgets import DateTimePicker

from .models import CustomUser, Event, DateTimeSlot


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'geographical_coordinates')
        widgets = {'geographical_coordinates': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        """makes not required fields in Django User model required """
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class CustomUserChangeForm(UserChangeForm):
    # UserChangeForm wants to change password as default, therefore it has to be overridden using "None"
    password = None

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email', 'geographical_coordinates']
        widgets = {'geographical_coordinates': forms.HiddenInput()}

    def __init__(self, *args, **kwargs):
        """makes not required fields in Django User model required """
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)


class CreateEventForm(forms.ModelForm):
    def __init__(self, *args, excluding_owner, **kwargs):
        """overriding default method which allows to exclude current user from queryset
        For it to work you have to add in views 'form = CreateEventForm(excluding_owner=request.user)' """
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(id=excluding_owner.pk)

    class Meta:
        model = Event
        fields = ["title", "description", "participants"]
        # TODO: consider changing in the future CheckboxSelectMultiple for some other widget
        widgets = {
            'participants': forms.CheckboxSelectMultiple,
        }


class ChooseMeetingLocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ChooseMeetingLocationForm, self).__init__(*args, **kwargs)
        self.fields['meeting_address'].widget.attrs['readonly'] = True
        self.fields['meeting_address'].label = False
        self.fields['location_comments'].label = "***Additional comments:**"

    class Meta:
        model = Event
        fields = ["meeting_address", "meeting_geographical_coordinates", "location_comments"]
        widgets = {'meeting_geographical_coordinates': forms.HiddenInput()}


class EditEventForm(forms.ModelForm):
    def __init__(self, *args, excluding_owner, **kwargs):
        """overriding default method , which allows to exclude current user from queryset
        For it to work you have to add in views form = CreateEventForm(excluding_owner=request.user)"""
        super(EditEventForm, self).__init__(*args, **kwargs)
        self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(pk=excluding_owner.pk)

    class Meta:
        model = Event
        fields = ['title', "description", 'participants']
        widgets = {
            'participants': forms.CheckboxSelectMultiple,
        }


class EditMeetingLocationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(EditMeetingLocationForm, self).__init__(*args, **kwargs)
        self.fields['meeting_address'].widget.attrs['readonly'] = True
        self.fields['meeting_address'].label = False
        self.fields['location_comments'].label = "***Additional comments:**"

    class Meta:
        model = Event
        fields = ["meeting_address", "meeting_geographical_coordinates", "location_comments"]
        widgets = {'meeting_geographical_coordinates': forms.HiddenInput()}


class CustomDatetimePicker(forms.ModelForm):
    class Meta:
        model = DateTimeSlot
        fields = ["date_time_from", "date_time_to"]
        widgets = {
            "date_time_from": DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
            "date_time_to": DateTimePicker(
                options={
                    'useCurrent': True,
                    'collapse': False,
                },
                attrs={
                    'append': 'fa fa-calendar',
                    'icon_toggle': True,
                }
            ),
        }

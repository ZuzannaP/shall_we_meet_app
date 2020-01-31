from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Event, DateTimeSlot
from tempus_dominus.widgets import DateTimePicker


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'geographical_coordinates')
        widgets = {'geographical_coordinates': forms.HiddenInput()}
        # fields = ('username', 'first_name', 'last_name', 'email', 'street', 'house_nr', 'zip_code', 'city')

    # added this part to make the on default not required fields in Django User model be required
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        # self.fields['house_nr'].help_text = "We ask only about house number. Don't provide additional flat number!"


class CustomUserChangeForm(UserChangeForm):
    # UserChangeForm wywołuje hasło, dlatego trzeba to nadpisać ustawiając "None"
    password = None

    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'email']
        # fields = ['first_name', 'last_name', 'email', 'street', 'house_nr', 'zip_code', 'city']

    # added this part to make the on default not required fields in Django User model be required
    def __init__(self, *args, **kwargs):
        super(CustomUserChangeForm, self).__init__(*args, **kwargs)

        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        # self.fields['house_nr'].help_text = "We ask only about house number. Don't provide additional flat number!"


class LoginForm(forms.Form):
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)


class CreateEventForm(forms.ModelForm):

    def __init__(self, *args, excluding_owner, **kwargs):
        '''overriding default method , which allows to exclude current user from queryset
        For it to work you have to add in views
        form = CreateEventForm(excluding_owner=request.user)'''
        super(CreateEventForm, self).__init__(*args, **kwargs)
        self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(id=excluding_owner.pk)

    class Meta:
        model = Event
        fields = ["title", "description", "location", "approx_duration", "participants"]
        # TODO: na razie jest to CheckboxSelectMultiple, ale co jak będzie więcej użytkowników?
        widgets = {
            'participants': forms.CheckboxSelectMultiple,
        }


class EditEventForm(forms.ModelForm):
    def __init__(self, *args, excluding_owner, **kwargs):
        '''overriding default method , which allows to exclude current user from queryset
        For it to work you have to add in views
        form = CreateEventForm(excluding_owner=request.user)'''
        super(EditEventForm, self).__init__(*args, **kwargs)
        self.fields['participants'].queryset = self.fields['participants'].queryset.exclude(pk=excluding_owner.pk)


    class Meta:
        model = Event
        fields = ['title', "description", 'location', 'approx_duration', 'participants']
        widgets = {
            'participants': forms.CheckboxSelectMultiple,
        }


class CustomDatetimePicker(forms.ModelForm):
    class Meta:  # model must be in the Meta class
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

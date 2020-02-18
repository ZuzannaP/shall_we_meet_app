"""shall_we_meet URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from perfect_slot.views import homepage, LoginView, LogoutView, SignUpView, EditPersonalInfoView, DeleteAccountView, \
    CustomPasswordChangeView, CustomPasswordChangeDoneView, CreateEventView, ChooseMeetingLocationView,\
    AccountSettingsView, EventView, OrganizerInProgressView, OrganizerUpcomingView, OrganizerArchiveView, \
    ProposeTimeslotsView, EditEventView, EditMeetingLocationView, DeleteEventView, EditOneTimeslotView, \
    EditTimeslotsView,AsGuestInProgressView, AsGuestUpcomingView, AsGuestArchiveView, VoteForTimeslotsView, VoteView,\
    CompleteEventView


urlpatterns = [
    path('manager/', admin.site.urls),
    path("", homepage, name="homepage"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('account/settings/', AccountSettingsView.as_view(), name='account_settings'),
    path('account/create/', SignUpView.as_view(), name='signup'),
    path('account/edit/', EditPersonalInfoView.as_view(), name="edit_personal_info"),
    path('account/delete/', DeleteAccountView.as_view(), name="delete_account"),
    path('password/change/', CustomPasswordChangeView.as_view(),  name='password_change'),
    path('password/change_done/', CustomPasswordChangeDoneView.as_view(), name='password_change_done'),
    path("event/create", CreateEventView.as_view(), name="create_event"),
    path("event/create/location/<int:event_id>/", ChooseMeetingLocationView.as_view(), name="choose_location"),
    path("event/create/timeslots/<int:event_id>/", ProposeTimeslotsView.as_view(), name="propose_timeslots"),
    path("event/edit/<int:pk>/", EditEventView.as_view(), name="edit_event"),
    path("event/edit/locations/<int:pk>/", EditMeetingLocationView.as_view(), name="edit_location"),
    path("event/edit/timeslots/<int:pk>/", EditTimeslotsView.as_view(), name="edit_timeslots"),
    path("event/edit/timeslot/<int:pk>/", EditOneTimeslotView.as_view(), name="edit_one_timeslot"),
    path("event/delete/<int:event_id>/", DeleteEventView.as_view(), name="delete_event"),
    path("event/view/<int:event_id>/", EventView.as_view(), name="event_view"),
    path("event/organizer/in_progress/", OrganizerInProgressView.as_view(), name="organizer_in_progress"),
    path("event/organizer/upcoming/", OrganizerUpcomingView.as_view(), name="organizer_upcoming"),
    path("event/organizer/archive/", OrganizerArchiveView.as_view(), name="organizer_is_archive"),
    path("event/guest/in_progress/", AsGuestInProgressView.as_view(), name="guest_in_progress"),
    path("event/guest/upcoming/", AsGuestUpcomingView.as_view(), name="guest_upcoming"),
    path("event/guest/archive/", AsGuestArchiveView.as_view(), name="guest_is_archive"),
    path("event/vote/timeslots/<int:event_id>/", VoteForTimeslotsView.as_view(), name="vote_for_timeslots"),
    path("event/vote/<int:timeslot_id>/<str:vote>/", VoteView.as_view(), name="vote"),
    path("event/complete/<int:event_id>/", CompleteEventView.as_view(), name="complete_event")

]

from django.test import TestCase
from django.test import Client
from django.urls import reverse

from perfect_slot.forms import CustomUserChangeForm, ChooseMeetingLocationForm, EditEventForm, \
                                EditMeetingLocationForm
from perfect_slot.models import CustomUser, Event, DateTimeSlot, ParticipantSlotVote


class ViewsUserTestClass(TestCase):
    def setUp(self):
        self.test_user = CustomUser.objects.create_user(first_name="Pan", last_name="Tester", username="pan_tester",
                                                        password="pantesterpantester", email="pan@wp.pl",
                                                        geographical_coordinates="Point(12 12)")

    def test_login(self):
        c = Client()
        response = c.login(username="pan_tester", password="pantesterpantester")
        self.assertTrue(response)

    def test_access_for_logged_in(self):
        c = Client()
        c.login(username="pan_tester", password="pantesterpantester")
        response = c.get(reverse("guest_in_progress"))
        self.assertEqual(response.status_code, 200)

    def test_restrictions_for_logged_out(self):
        """ logged-out user can not access urls restricted for logged-in users """
        c = Client()
        c.logout()
        response = c.get(reverse("guest_in_progress"))
        self.assertRedirects(response, "/login/?next=/event/guest/in_progress/")


class ViewsAppLogicTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.test_user = CustomUser.objects.create_user(first_name="Pan", last_name="Tester", username="pan_tester",
                                               password="pantesterpantester", email="pan@wp.pl",
                                               geographical_coordinates="Point(12 12)")
        cls.test_participant = CustomUser.objects.create_user(first_name="Pan2", last_name="Tester2", username="pan_tester2",
                                               password="pantester2pantester2", email="pan2@wp.pl",
                                               geographical_coordinates="Point(12 12)")
        cls.test_event = Event.objects.create(title="My event", description="Great event", owner=cls.test_user)
        cls.test_event.participants.add(cls.test_participant)
        cls.test_datetimeslot = DateTimeSlot.objects.create(date_time_from="2021-03-18 17:30:00+01",
                                            date_time_to="2021-03-18 20:00:00+01", event=cls.test_event)
        cls.test_participantslotvote = ParticipantSlotVote.objects.create(participant=cls.test_participant,
                                                                          slot=cls.test_datetimeslot, vote=1)
        cls.client = Client()

    def test_create_event_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('create_event'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'create_event_tmp.html')

    def test_choose_meeting_location_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('choose_location', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'choose_meeting_location_tmp.html')

    def test_propose_timeslots_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('propose_timeslots', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'propose_time_slots_tmp.html')

    def test_event_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('event_view', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'view_event_tmp.html')

    def test_complete_event_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('complete_event', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'complete_event_tmp.html')

    def test_edit_event_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('edit_event', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_event_tmp.html')

    def test_edit_meeting_location_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('edit_location', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_meeting_location_tmp.html')

    def test_edit_timeslots_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('edit_timeslots', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_time_slots_tmp.html')

    def test_edit_one_timeslot_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('edit_one_timeslot', args=(self.test_datetimeslot.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'edit_one_time_slot_tmp.html')

    def test_delete_event_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester", password="pantesterpantester")
        response = self.client.get(reverse('delete_event', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete_event_tmp.html')

    def test_vote_for_timeslots_view_uses_correct_template_and_has_desired_location(self):
        self.client.login(username="pan_tester2", password="pantester2pantester2")
        response = self.client.get(reverse('vote_for_timeslots', args=(self.test_event.pk,)))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'vote_for_timeslots_tmp.html')

    def test_vote_view_has_desired_location(self):
        self.client.login(username="pan_tester2", password="pantester2pantester2")
        response = self.client.get(reverse('vote', args=(self.test_datetimeslot.pk, self.test_participantslotvote.pk,)))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('vote_for_timeslots', args=(self.test_participantslotvote.pk,)))


class ModelTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c = CustomUser.objects.create_user(first_name="Pan", last_name="Tester", username="pan_tester",
                                               password="pantesterpantester", email="pan@wp.pl",
                                               geographical_coordinates="Point(12 12)")
        cls.e = Event.objects.create(title="My event", description="Great event", owner=cls.c)
        cls.d = DateTimeSlot.objects.create(date_time_from="2021-03-18 17:30:00+01",
                                            date_time_to="2021-03-18 20:00:00+01", event=cls.e)
        cls.p = ParticipantSlotVote.objects.create(participant=cls.c, slot=cls.d, vote=1)

    def test_user(self):
        self.assertTrue(isinstance(self.c, CustomUser))
        self.assertEqual(self.c.__str__(), self.c.username)

    def test_event(self):
        self.assertTrue(isinstance(self.e, Event))
        self.assertEqual(self.e.__str__(), self.e.title)

    def test_datetime_slot(self):
        self.assertTrue(isinstance(self.d, DateTimeSlot))
        self.assertEqual(self.d.__str__(), f"{self.d.date_time_from} - {self.d.date_time_to}")

    def test_participant_slot_vote(self):
        self.assertTrue(isinstance(self.p, ParticipantSlotVote))
        self.assertEqual(self.p.__str__(), f"{self.p.participant}-{self.p.slot}: {self.p.vote}")


class FormsTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.c = CustomUser.objects.create_user(first_name="Pan", last_name="Tester", username="pan_tester",
                                               password="pantesterpantester", email="pan@wp.pl",
                                               geographical_coordinates="Point(12 12)")
        cls.e = Event.objects.create(title="My event", description="Great event", owner=cls.c)
        cls.d = DateTimeSlot.objects.create(date_time_from="2021-03-18 17:30:00+01",
                                            date_time_to="2021-03-18 20:00:00+01", event=cls.e)
        cls.p = ParticipantSlotVote.objects.create(participant=cls.c, slot=cls.d, vote=1)

    def test_valid_custom_user_change_form(self):
        self.c = CustomUser.objects.create_user(first_name="Pan1", last_name="Tester1", username="pan_tester1",
                                                password="pantester1pantester1", email="pan1@wp.pl",
                                                geographical_coordinates="Point(12 12)")
        data = {'first_name': self.c.first_name, 'last_name': self.c.last_name, 'email': self.c.email,
                'geographical_coordinates': self.c.geographical_coordinates}
        form = CustomUserChangeForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_custom_user_change_form(self):
        self.c = CustomUser.objects.create_user(first_name="Pan2", last_name="Tester2", username="pan_tester2",
                                                password="pantester2pantester2", email="",
                                                geographical_coordinates="Point(12 12)")
        data = {'first_name': self.c.first_name, 'last_name': self.c.last_name, 'email': self.c.email,
                'geographical_coordinates': self.c.geographical_coordinates}
        form = CustomUserChangeForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_choose_meeting_location_form(self):
        self.e.meeting_address = "Nice Street"
        self.e.meeting_geographical_coordinates = "Point(13 13)"
        self.e.location_comments = "The key is under doormat"
        data = {'meeting_address': self.e.meeting_address,
                "meeting_geographical_coordinates": self.e.meeting_geographical_coordinates,
                "location_comments": self.e.location_comments}
        form = ChooseMeetingLocationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_choose_meeting_location_form(self):
        """omitting "meeting_geographical_coordinates" on purpose"""
        self.e.meeting_address = "Big Street"
        self.e.meeting_geographical_coordinates = "Point(13 13)"
        self.e.location_comments = "The key is vase"
        data = {'meeting_address': self.e.meeting_address,
                "meeting_geographical_coordinates": "",
                "location_comments": self.e.location_comments}
        form = ChooseMeetingLocationForm(data=data)
        self.assertFalse(form.is_valid())

    def test_valid_edit_event_form(self):
        self.test_participant = CustomUser.objects.create_user(first_name="PanPat", last_name="Participant",
                                                               username="pan_participant",
                                                               password="pan_participantpan_participant",
                                                               email="participant@wp.pl",
                                                               geographical_coordinates="Point(14 14)")
        self.e.participants.add(self.test_participant)
        form = EditEventForm(excluding_owner=self.c)
        displayed_participants = form.fields['participants'].queryset.all()
        self.assertTrue(self.c not in displayed_participants)

    def test_valid_edit_meeting_location_form(self):
        self.e.meeting_address = "Big Street"
        self.e.meeting_geographical_coordinates = "Point(4 4)"
        self.e.location_comments = "There are no doors. Use window"
        data = {'meeting_address': self.e.meeting_address,
                "meeting_geographical_coordinates": self.e.meeting_geographical_coordinates,
                "location_comments": self.e.location_comments}
        form = EditMeetingLocationForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_edit_meeting_location_form(self):
        """omitting "meeting_address" on purpose"""
        self.e.meeting_address = "Big Street"
        self.e.meeting_geographical_coordinates = "Point(4 4)"
        self.e.location_comments = "There are no doors. Use window"
        data = {'meeting_address': "",
                "meeting_geographical_coordinates": self.e.meeting_geographical_coordinates,
                "location_comments": self.e.location_comments}
        form = EditMeetingLocationForm(data=data)
        self.assertFalse(form.is_valid())
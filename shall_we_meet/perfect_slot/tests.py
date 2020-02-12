from django.test import TestCase
from django.test import Client
from django.urls import reverse

from perfect_slot.models import CustomUser, Event


class ViewsTestClass(TestCase):
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
        """ logged out user can not access urls restricted for logged in users """
        c = Client()
        c.logout()
        response = c.get(reverse("guest_in_progress"))
        self.assertRedirects(response, "/login/?next=/event/guest/in_progress/")


class FormsTestClass(TestCase):
    # def setUp(self):
    #     print("setUp: Run once for every test method to setup clean data.")
    #     pass

    def test_mock(self):
        u = 4
        self.assertEqual(u, 1)
        print("do stuff4")


class ModelTestClass(TestCase):
    def setUp(self):
        self.test_event = Event.objects.create(title="My event", description="Great event")
        print("do stuff5")

    def test_my(self):
        e = Event.objects.get(pk=1)
        self.assertEqual(e.title, "My event")
        print("do stuff6")
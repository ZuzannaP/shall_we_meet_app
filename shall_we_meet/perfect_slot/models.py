from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE, SET_NULL


# zauważ, że używasz tego tylko po to, by mieć models.PointField(). Oznacza to, że jeśli zdecydujesz się zmienić w \
# modelu w Event oraz User     geographical_coordinates = models.PointField() na\
# models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True) to skasuj poniższy import z GIS
# Note "X and Y coordinates".
# so, if you're coming from google maps, and experienced to latlng objects and the like, x and y are like switched.\
# this caused my some headache! X is longitude, Y is latitude.

# from django.contrib.gis.db import models


class CustomUser(AbstractUser):
    street = models.CharField(max_length=128)
    house_nr = models.CharField(max_length=10)
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=128)
    # geographical_coordinates = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    approx_duration = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    participants = models.ManyToManyField(CustomUser)
    owner = models.ForeignKey(CustomUser, on_delete=CASCADE)
    is_active = models.BooleanField(default=False)

    # # to trzeba zmienić z pointfield na obiekt przechowujący cały obszar geograficzny
    # common_geographical_coordinates = models.PointField(blank=True, null=True)
    # # to trzeba zmienić z pointfield na obiekt przechowujący cały obszar geograficzny
    # proposed_location = models.PointField(blank=True, null=True)
    # final_location = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.title


class DateTimeSlots(models.Model):
    date_time_from = models.DateTimeField()
    date_time_to = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=CASCADE)
    participant = models.ManyToManyField(CustomUser)
    winning = models.BooleanField(default=False)
    # votes_yes = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0)])
    # votes_no = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0)])
    # votes_if_need_be = models.IntegerField(blank=True, default=0, validators=[MinValueValidator(0)])

    def __str__(self):
        return f"{self.date_time_from}-{self.date_time_to}"

from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE
from django.contrib.gis.db import models

#  X is longitude, Y is latitude.

class CustomUser(AbstractUser):
    geographical_coordinates = models.PointField()

    def __str__(self):
        return self.username


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    location = models.CharField(max_length=256) # do usunięcia ,jak będzie druga aplikacja
    creation_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    approx_duration = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    participants = models.ManyToManyField(CustomUser, related_name='their_events')
    owner = models.ForeignKey(CustomUser, on_delete=CASCADE, related_name='his_events')
    is_in_progress = models.BooleanField(default=True)
    is_upcoming = models.BooleanField(default=False)
    is_archive = models.BooleanField(default=False)

    # # to trzeba zmienić z pointfield na obiekt przechowujący cały obszar geograficzny (polygonfield?)
    # common_geographical_coordinates = models.PointField(blank=True, null=True)

    # # to trzeba zmienić z pointfield na obiekt przechowujący cały obszar geograficzny
    # proposed_location = models.PointField(blank=True, null=True)
    # final_location = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.title


class DateTimeSlot(models.Model):
    date_time_from = models.DateTimeField()
    date_time_to = models.DateTimeField()
    event = models.ForeignKey(Event, on_delete=CASCADE, related_name="event_datetimeslot")
    participants = models.ManyToManyField(CustomUser, through='ParticipantSlotVote')
    winning = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.date_time_from} - {self.date_time_to}"


class ParticipantSlotVote(models.Model):
    participant = models.ForeignKey(CustomUser, on_delete=CASCADE, related_name='his_slots_votes')
    slot = models.ForeignKey(DateTimeSlot, on_delete=CASCADE, related_name='participants_votes')
    vote = models.SmallIntegerField(default=-2, choices=[(-2, "Did not vote"), (1, "No"), (3, "If need be"), (2, "Yes")])

    def __str__(self):
        return f"{self.participant}-{self.slot}: {self.vote}"

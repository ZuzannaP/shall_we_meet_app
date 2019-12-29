from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models import CASCADE, PROTECT

# zauważ, że używasz tego tylko po to, by mieć models.PointField(). Oznacza to, że jeśli zdecydujesz się zmienić w \
# modelu w Event oraz User     geographical_coordinates = models.PointField() na\
# models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True) to skasuj poniższy import z GIS
# Note "X and Y coordinates".
# so, if you're coming from google maps, and experienced to latlng objects and the like, x and y are like switched.\
# this caused my some headache! X is longitude, Y is latitude.
from django.contrib.gis.db import models


class Event(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    meeting_duration = models.SmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(12)])
    proposed_datetime_slots = models.ManyToManyField(DateTimeSlots)
    final_datetime_slot = models.ForeignKey(DateTimeSlots, null=True, blank=True, on_delete=PROTECT)
    #pamiętaj by zmienić User na coś innego, jak się okaże, że korzystamy z innego usera
    participants = models.ManyToManyField(User)
    #pamiętaj by zmienić User na coś innego, jak się okaże, że korzystamy z innego usera
    owner = models.ForeignKey(User, on_delete=CASCADE)
    # to trzeba zmienić z pointfield na obiekt przechowujący cały obszar geograficzny
    common_geographical_coordinates = models.PointField(blank=True, null=True)
    # to trzeba zmienić z pointfield na obiekt przechowujący cały obszar geograficzny
    proposed_location = models.PointField(blank=True, null=True)
    final_location = models.PointField(blank=True, null=True)

    def __str__(self):
        return self.title


class User(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    #czy ja w ogóle mam tworzyć użytkownika, skoro on przy tworzeniu konta się stworzy i tak???????????????? jak tu zrobić interakcję między logującymi sę użytkownikami a tym, zeby można było zapraszać użytkownikóœ?
    password = models.?????????????????????????????
    # sprawdź w necie jak najlepiej trzymać polskie adresy w django
    street = models.CharField(max_length=128)
    house_nr = models.CharField(max_length=10)
    #wybierz od 00-001 do  05-077
    zip_code = models.CharField(max_length=6)
    city = models.CharField(max_length=128)
    country_of_residence = models.ChoiceField(choices=[("Poland", "Poland")], default = "Poland")
    geographical_coordinates = models.PointField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class DateTimeSlots(models.Model):
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.date} {self.start_time}-{self.end_time}"

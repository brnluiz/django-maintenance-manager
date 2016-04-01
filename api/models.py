from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class UserCommonInfo(models.Model):
    phone      = models.CharField(max_length=20)
    # Dates:
    created_at = models.DateTimeField(auto_now=True)
    # Foreign Keys
    user       = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True

# Location classes: will be used to indicate which flat have problems
class Location(models.Model):
    postal   = models.CharField(max_length=15)
    city     = models.CharField(max_length=50)
    address  = models.CharField(max_length=100)
    building = models.CharField(max_length=75)

class Flat(models.Model):
    identificator = models.CharField(max_length=15)
    # Foreign Keys:
    location      = models.ForeignKey(Location, related_name='flats', on_delete=models.CASCADE)

class Room(models.Model):
    identificator = models.CharField(max_length=15)
    # Foreign Keys:
    flat          = models.ForeignKey(Flat, related_name='rooms', on_delete=models.CASCADE)

# Resident class: a simple register for the resident/student

# Role system to organizer staff
class Role(models.Model):
    title = models.CharField(max_length=50)
    level = models.IntegerField()

# User Profiles (for resident and staff)
class Resident(UserCommonInfo):
    # Foreign Keys:
    room       = models.ForeignKey(Room, related_name='resident', on_delete=models.CASCADE)

class Staff(UserCommonInfo):
    # Foreign Keys:
    role       = models.ForeignKey(Role, related_name='staffs', on_delete=models.CASCADE)

# Report and Enquire details:
class Status(models.Model):
    title   = models.CharField(max_length=70)
    urgency = models.IntegerField()

class Enquire(models.Model):
    reference   = models.CharField(max_length=10)
    title       = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    # Dates:
    created_at  = models.DateTimeField(auto_now=True)
    # Foreign Keys:
    status      = models.ForeignKey(Status, related_name='enquires', on_delete=models.CASCADE)
    resident    = models.ForeignKey(Resident, related_name='enquires', on_delete=models.CASCADE)
    location    = models.ForeignKey(Location, related_name='enquires', on_delete=models.CASCADE)

class Report(models.Model):
    reference   = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    # Dates:
    created_at  = models.DateTimeField(auto_now=True)
    # Foreign Keys:
    enquire     = models.ForeignKey(Enquire, related_name='reports', on_delete=models.CASCADE)
    staff       = models.ForeignKey(Staff, related_name='reports', on_delete=models.CASCADE)
    status      = models.ForeignKey(Status, related_name='reports', on_delete=models.CASCADE)
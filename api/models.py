from __future__ import unicode_literals

from django.db import models

# Create your models here.

# Location classes: will be used to indicate which flat have problems
class Location(models.Model):
    postal   = models.CharField(max_length=15)
    city     = models.CharField(max_length=50)
    address  = models.CharField(max_length=100)
    building = models.CharField(max_length=75)

class Flat(models.Model):
    identificator = models.CharField(max_length=15)
    # Foreign Keys:
    location      = models.ForeignKey(Location, on_delete=models.CASCADE)

class Room(models.Model):
    identificator = models.CharField(max_length=15)
    # Foreign Keys:
    flat          = models.ForeignKey(Flat, on_delete=models.CASCADE)

# User class: a simple register for the user/student
class User(models.Model):
    name      = models.CharField(max_length=50)
    surname   = models.CharField(max_length=50)
    email     = models.EmailField()
    phone     = models.BigIntegerField()
    # Dates:
    createdAt = models.DateTimeField('created date')
    # Foreign Keys:
    place     = models.ForeignKey(Room, on_delete=models.CASCADE)

# Employee register: have a role system to limit the technician inserts
class Role(models.Model):
    title = models.CharField(max_length=50)
    level = models.IntegerField()

class Employee(models.Model):
    name      = models.CharField(max_length=50)
    surname   = models.CharField(max_length=50)
    email     = models.EmailField()
    phone     = models.BigIntegerField()
    # Dates:
    createdAt = models.DateTimeField('created date')
    # Foreign Keys:
    role      = models.ForeignKey(Role, on_delete=models.CASCADE)

# Report and Enquire details:
class Status(models.Model):
    reference   = models.CharField(max_length=70)
    urgency     = models.IntegerField()

class Enquire(models.Model):
    reference   = models.CharField(max_length=10)
    title       = models.CharField(max_length=100)
    description = models.TextField()
    # Dates:
    createdAt   = models.DateTimeField('created date')
    # Foreign Keys:
    status      = models.ForeignKey(Status, on_delete=models.CASCADE)
    user        = models.ForeignKey(User, on_delete=models.CASCADE)
    place       = models.ForeignKey(Room, on_delete=models.CASCADE)

class Report(models.Model):
    enquire     = models.ForeignKey(Enquire, on_delete=models.CASCADE)
    reference   = models.CharField(max_length=10)
    description = models.TextField()
    reference   = models.CharField(max_length=10)
    # Dates:
    createdAt   = models.DateTimeField('created date')
    # Foreign Keys:
    employee    = models.ForeignKey(Location, on_delete=models.CASCADE)
    status      = models.ForeignKey(Status, on_delete=models.CASCADE)
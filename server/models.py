__author__ = 'mpetyx'

from django.contrib.auth.models import User
from django.db import models

class Value(models.Model):
    timestamp = models.DateField(auto_now_add=True)
    metric = models.TextField()

class Buffer(models.Model):
    description = models.TextField()
    refresh_rate = models.FloatField()
    created = models.DateField()
    updated = models.DateField()
    state = models.BooleanField(default=True)
    label = models.TextField()

class Plug(Buffer):
    # Prizes mono On/Off
    pass

class Sensor(Buffer):
    # analink + digital for movement sensor
    values = models.ManyToManyField(Value, null=True, blank=True)

class Counter(Buffer):
    #
    kwatt = models.OneToOneField(Value,related_name="1")
    kwh1 = models.OneToOneField(Value,related_name="2")
    kwh2 = models.OneToOneField(Value,related_name="3")
    kwh3 = models.OneToOneField(Value,related_name="4")
    kwhtotal = models.OneToOneField(Value,related_name="5")
    voltage = models.OneToOneField(Value,related_name="6")
    ampere = models.OneToOneField(Value,related_name="7")
    pf = models.OneToOneField(Value,related_name="8")

class Building(models.Model):
    pass

class ElectriCar(models.Model):
    pass

class StreetLighting(models.Model):
    pass

from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Member(models.Model):
    firstname = models.CharField(max_length=40, blank=False)
    lastname = models.CharField(max_length=40, blank=False)
    mobile_number = models.CharField(max_length=10, blank=True)
    description = models.TextField(max_length=255, blank=False)
    location = models.TextField(max_length=255, blank=False)
    date = models.DateField('%m/%d/%Y')
    created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
    updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')

class Car(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.CharField(max_length=40, blank=False)
    typeofcar = models.CharField(max_length=10, blank=True)
    speed = models.TextField(max_length=255, blank=False)
    startdate = models.DateField('%m/%d/%Y')



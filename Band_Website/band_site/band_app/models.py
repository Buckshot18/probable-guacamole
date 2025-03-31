from django.db import models
from django.contrib.auth.models import User

class BandMember(models.Model):
    name = models.CharField(max_length=100)
    instrument = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name

class Event(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateField()
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.title

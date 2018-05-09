from __future__ import unicode_literals

from django.db import models
from ..logReg_app .models import User
# Create your models here.
class Trip(models.Model):
    traveler = models.ForeignKey(User, related_name = "trips")
    destination = models.CharField(max_length=50)
    start_date = models.DateField(auto_now=False, auto_now_add=False)
    end_date = models.DateField(auto_now=False, auto_now_add=False)
    desc = models.CharField(max_length=255)
    all_users = models.ManyToManyField(User, related_name="all_trips")
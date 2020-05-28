import datetime
from django.db.models.signals import post_save
from django.db import models
from django.utils import timezone
from django.dispatch import receiver


class Player(models.Model):
    name = models.CharField(max_length = 130)
    email = models.EmailField(blank=True)
    no_tickets = models.IntegerField(default=0)
    def __str__(self):
        return self.name

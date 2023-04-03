from django.db import models

# Create your models here.
class Room(models.Model):
    roomName = models.CharField(max_length=255)
    num_seats = models.IntegerField()
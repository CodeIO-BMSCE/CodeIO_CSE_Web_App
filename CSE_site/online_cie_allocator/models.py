from django.db import models

# Create your models here.
class Room(models.Model):
    roomName = models.CharField(max_length=255, primary_key=True)
    num_seats = models.IntegerField()

    def __str__(self):
        return "<Room " + self.usn + ">"
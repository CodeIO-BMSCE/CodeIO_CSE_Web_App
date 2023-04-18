from django.db import models
from datetime import datetime

# Create your models here.

# class Chat(models.Model): 
#     text = models.TextField() 
    
#     def __str__(self):
#         return self.text

class Room(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=25)

class Message(models.Model):
    # room = models.ForeignKey("Room", on_delete=models.CASCADE, max_length=25)
    value = models.CharField(max_length=500)
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.CharField(max_length=25)
    room = models.CharField(max_length=25)
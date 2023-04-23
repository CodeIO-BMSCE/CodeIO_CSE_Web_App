import uuid
from django.db import models

class Course_Type(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Course(models.Model):
    code = models.CharField(max_length=255, primary_key=True)
    title = models.CharField(max_length=255)
    sem = models.IntegerField()
    # batch = models.IntegerField()
    type = models.ForeignKey(Course_Type, on_delete=models.PROTECT)

    def __str__(self):
        return "<Course " + self.code + ">"
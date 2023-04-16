from django.db import models
from authentication.models import Student
from CSE_site.models import Course

# Rooms where exams are to be conducted
class Room(models.Model):
    roomName = models.CharField(max_length=255, primary_key=True)
    num_seats = models.IntegerField()

    def __str__(self):
        return "<Exam Room " + self.usn + ">"
    
class Assigned_Exam_Room(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.PROTECT, primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT, primary_key=True)
    room_name = models.ForeignKey(Room, on_delete=models.PROTECT)

    def __str__(self):
        return "<Exam Room " + self.usn + ">"
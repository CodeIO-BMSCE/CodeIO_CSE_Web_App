from django.db import models
from authentication.models import Student
from CSE_site.models import Course, Exam

# Rooms where exams are to be conducted
class Room(models.Model):
    roomName = models.CharField(max_length=255, primary_key=True)
    num_seats = models.IntegerField()

    def __str__(self):
        return "<Exam Room " + self.roomName + ">"
    
class Assigned_Exam_Room(models.Model):
    stud_id = models.ForeignKey(Student, on_delete=models.PROTECT)
    course_id = models.ForeignKey(Course, on_delete=models.PROTECT)
    exam_id = models.ForeignKey(Exam, on_delete=models.PROTECT)
    # room_name = models.ForeignKey(Room, on_delete=models.PROTECT)
    room_number = models.IntegerField(null=True) # TODO: make null: False

    def __str__(self):
        return "<Assigned " + self.stud_id.usn + " to room " + str(self.room_number) + " for " + self.course_id.code + " " + self.exam_id.title + ">"
    
    class Meta:
        ordering = ['stud_id', 'exam_id']
        constraints = [
            models.UniqueConstraint(
                fields=['stud_id', 'course_id', 'exam_id'], name='unique_stud_id_course_id_exam_id_combination'
            )
        ]
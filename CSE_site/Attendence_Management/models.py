from django.db import models
from django.utils import timezone

# Create your models here.
class Attendance(models.Model):
   
    attendance = models.TextField()
    date= models.DateField(default=timezone.now)
    section = models.CharField(max_length=2 , blank=False , null=True)
    courseTitle = models.CharField(max_length=25 , blank=False , null=True)
        

    
class FacultyCourse(models.Model):
    courseTitle = models.CharField(max_length=25)
    courseCode = models.CharField(max_length=10)
    semester = models.CharField(max_length=1)
    section = models.CharField(max_length=1)
    faculty = models.CharField(max_length=30)
    academicYear = models.CharField(max_length=7)
        
    def __str__(self):
        return self.courseTitle


class Student(models.Model):
    name=models.CharField(max_length=50)
    usn=models.CharField(max_length=10,unique=True)
    email = models.EmailField(unique=True)
    section=models.CharField(max_length=2)

    class Meta:
        ordering = ['usn']
        
    def __str__(self):
        return self.usn

 
class Course(models.Model):
    className = models.CharField(max_length=2)
    courses = models.TextField()
    facultyHandles = models.TextField()
        
    def __str__(self):
        return self.className

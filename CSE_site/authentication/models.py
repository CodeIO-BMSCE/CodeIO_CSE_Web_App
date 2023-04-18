from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver

from .managers import CustomUserManager
# from CSE_site.models import Student_Batch
from CSE_site.models import Course

class User(AbstractUser):
    username = None
    first_name = None
    last_name = None
    
    email = models.EmailField(primary_key=True)
    name = models.CharField(max_length=255)
    is_email_verified = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email.split('@')[0]

class Student(User):
    usn = models.CharField(max_length=255, unique=True)
    join_year = models.IntegerField()
    current_sem = models.IntegerField(null=True)
    courses = models.ManyToManyField(Course)
    # batch = models.ForeignKey(Student_Batch, on_delete=models.PROTECT)

    def __str__(self):
        return "<Student " + self.usn + ">"

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"

class Faculty(User): 
    designation = models.CharField(max_length=255)

    def __str__(self):
        return "<Faculty " + self.email + ">"
    
    class Meta:
        verbose_name = "Faculty"
        verbose_name_plural = "Faculties"


class Office(User):
    location = models.CharField(max_length=255)

    def __str__(self):
        return "<Office " + self.email + ">"
    
    class Meta:
        verbose_name = "Office"
        verbose_name_plural = "Office"


from django.contrib import admin

from .models import Room, Assigned_Exam_Room



# Register your models here.
admin.site.register(Room)
admin.site.register(Assigned_Exam_Room)
from django.contrib import admin

from .models import Course, Course_Type

admin.site.register(Course)
admin.site.register(Course_Type)
# admin.site.register(Student_Batch)
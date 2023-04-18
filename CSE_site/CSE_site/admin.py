from django.contrib import admin

from .models import Course, Course_Type, Exam, Exam_Type

admin.site.register(Course)
admin.site.register(Course_Type)
admin.site.register(Exam)
admin.site.register(Exam_Type)
# admin.site.register(Student_Batch)
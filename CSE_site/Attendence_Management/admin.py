from django.contrib import admin
from . import models


# Register your models here.
admin.site.register(models.Attendance)
admin.site.register(models.FacultyCourse)
admin.site.register(models.Student)
admin.site.register(models.Course)

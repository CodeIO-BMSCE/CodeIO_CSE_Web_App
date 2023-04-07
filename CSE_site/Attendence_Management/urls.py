from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('studentdashboard/',StudentDashboard , name='studentdashboard'),
    path('studentcourse/',StudentCourse , name='studentcourse'),
    path('facultycourses/', facultyCourses , name='facultyCourses'),
    # path('facultysections/',facultySections , name='facultySections'),
    path('facultyattendance/',facultyAttendance , name='facultyAttendance'),
    path('logout/' , Logout , name='logout'),
]
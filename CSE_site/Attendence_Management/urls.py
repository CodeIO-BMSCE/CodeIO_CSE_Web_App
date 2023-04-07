from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('studentdashboard/',StudentDashboard , name='studentdashboard'),
    path('studentcourse/',StudentCourse , name='studentcourse'),
    path('facultycourses/', facultyCourses , name='facultyCourses'),
    path('facultyattendance/',facultyAttendance , name='facultyAttendance'),
    path('studentList/', studentList , name='studentList'),
    path('logout/' , Logout , name='logout'),
]
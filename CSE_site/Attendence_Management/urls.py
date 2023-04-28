from django.urls import path, include
from .views import *

urlpatterns = [
    # path('', home, name='home'),
    path('studentdashboard/',StudentDashboard , name='studentdashboard'),
    path('studentcourse/',StudentCourse , name='studentcourse'),
    path('facultycourses/', facultyCourses , name='facultyCourses'),
    path('facultycourses/<str:course_code>/<str:section>', updateCourse, name="updateCourse"),
    path('facultycourses/<str:course_title>/<str:course_code>/<str:section>', deleteCourse, name="deleteCourse"),
    path('facultycourses/<str:academic_year>', academicyear, name="academicyear"),
    path('facultyattendance/',facultyAttendance , name='facultyAttendance'),
    path('studentList/', studentList , name='studentList'),
    path('logout/' , Logout , name='logout'),
]
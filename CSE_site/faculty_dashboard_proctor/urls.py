from django.urls import path,include
from . import views

app_name = 'faculty'

urlpatterns = [
    path('/dashboard/', views.dashboard, name="dashboard"),
    path('/student/<str:pk>', views.studentDetails, name="student-details"),
    path('/student/approved/<str:pk>', views.approve, name="student-details-approve"),
    path('/student/approved/<str:pk>/<str:course_id>', views.courseApprove, name="student-course-approve"),
    path('/student/reject/<str:emails>', views.courseReject, name='student-course-reject'),
<<<<<<< HEAD
    # path('/add-students', views.addStudents, name='add-students')
=======
    path('/add-students', views.addStudents, name='add-students'),
    path('/add-marks', views.addMarks, name='add-marks'),
    path('/send-register-form', views.sendCourse, name='send-register-form'),
    path('/student/alert/<str:emails>', views.sendAlertMail, name='student-alert'),
>>>>>>> main
]
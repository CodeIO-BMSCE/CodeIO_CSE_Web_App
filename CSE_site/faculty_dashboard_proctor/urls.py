from django.urls import path,include
from . import views

app_name = 'faculty'

urlpatterns = [
    path('/dashboard/', views.dashboard, name="dashboard"),
    path('/student/<str:pk>', views.studentDetails, name="student-details"),
    path('/student/approved/<str:pk>', views.approve, name="student-details-approve"),
    path('/student/approved/<str:pk>/<str:course_id>', views.courseApprove, name="student-course-approve"),
    path('/student/reject/<str:emails>', views.courseReject, name='student-course-reject'),
    path('/student/fapproved/<str:pk>/<str:course_id>', views.courseApproveFast, name="student-fcourse-approve"),
    path('/student/freject/<str:emails>', views.courseRejectFast, name='student-fcourse-reject'),
    path('/add-students', views.addStudents, name='add-students'),
    path('/add-marks', views.addMarks, name='add-marks'),
    path('/send-register-form', views.sendCourse, name='send-register-form'),
    path('/student/alert/<str:emails>', views.sendAlertMail, name='student-alert'),
    path('/send-email-parent', views.sendParents, name="send-parents"),
    path('/send-email-custom', views.writeEmail, name='custom-email'),
    path('/email-form', views.customMail, name='custom-form'),
    path('/add-marks-fast', views.addfastMarks, name='add-marks-fast')
]
from django.urls import path,include
from . import views

app_name = 'student'

urlpatterns = [
    path('/dashboard/<str:pk>/', views.dashboard, name="dashboard"),
    path('/marks/<str:pk>/', views.dashboard_marks, name="marks"),
    path('/courses/register/', views.registerCourses, name='register'),
    path('/add_student_details/', views.studentDetails, name='student_details_form'),
    path('/courses/edit/', views.editCourseDetails, name='edit'),
    path('/courses/update/', views.updateCourseDetails, name='update'),
    path("/no_proctor", views.no_proc, name="no_proctor"),
    path("/courses/fastrack/register", views.registerFastrack, name="fastrack_register"),
]

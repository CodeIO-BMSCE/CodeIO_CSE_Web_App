from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_allocator, name="exam_allocator"),
    path('student/', views.student_dashboard, name='exam_allocator_student_dashboard'),
    path('office/', views.office_dashboard, name='exam_allocator_office_dashboard'),
    path('office/semester/<int:sem>', views.office_semester_view, name="exam_allocator_office_semester_view"),
    path('office/download_template/<int:semester>', views.office_download_template, name="exam_allocator_office_download_template"),
    path('office/upload', views.office_upload, name="exam_allocator_office_upload"),
    path('faculty/', views.faculty_view, name="exam_allocator_faculty_view"),
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.exam_allocator, name="exam_allocator"),
    path('office/', views.office_dashboard_view, name='exam_allocator_office_dashboard'),
    path('office/assign/students/', views.office_assign_students_view, name='exam_allocator_office_assign_students'),
    path('office/assign/students/download_template/<str:course_code>/', views.office_assign_students_download_template, name='exam_allocator_office_assign_students_download_template'),
    path('office/assign/students/upload/', views.office_assign_students_upload, name='exam_allocator_office_assign_students_upload'),
    path('office/assign/invigilators/', views.office_assign_invigilators_view, name='exam_allocator_office_assign_invigilators'),
    path('office/assign/invigilators/download_template/', views.office_assign_invigilators_download_template, name='exam_allocator_office_assign_invigilators_download_template'),
    path('office/assign/invigilators/upload/', views.office_assign_invigilators_upload, name='exam_allocator_office_assign_invigilators_upload'),
]
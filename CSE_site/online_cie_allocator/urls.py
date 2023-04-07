from django.urls import path
from . import views

urlpatterns = [
    path('office', views.office_view, name='cie_allocator_office_view'),
    path('student', views.student_view, name='cie_allocator_student_view'),
]
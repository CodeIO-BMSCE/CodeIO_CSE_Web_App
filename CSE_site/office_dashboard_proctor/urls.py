from django.urls import path,include
from . import views

app_name = 'office'

urlpatterns = [
    path('/dashboard/', views.dashboard, name="dashboard"),
    path('/proctor-assign', views.proctor_assign, name='proctor-assign'),
    path('/download-excel/', views.download_excel, name='download-excel'),
    path('/view-students/<str:pk>', views.view_students, name='view-proctor-students'),

]
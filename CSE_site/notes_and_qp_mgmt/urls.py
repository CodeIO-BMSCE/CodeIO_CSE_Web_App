from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.upload, name='upload'),
    path('pdf_view/<str:path>/<str:file>', views.pdf_view, name='pdf_view'),
]




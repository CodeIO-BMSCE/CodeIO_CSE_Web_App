from django.urls import path, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.auth_home, name='auth_home'),
    path('register/', views.register_home, name="auth_register_home"),
    path('login/', views.login_home, name="auth_login_home"),
    path('register/student/', views.register_student, name='auth_register_student'),
    path('login/student/', views.login_student, name='auth_login_student'),
    path('register/faculty/', views.register_faculty, name='auth_register_faculty'),
    path('login/faculty/', views.login_faculty, name='auth_login_faculty'),
    path('login/office/', views.login_office, name='auth_login_office'),
    path('logout/', views.logout_user, name="auth_logout"),
    path('verify_email/<uidb64>/<token>/', views.verify_email, name="auth_verify_email"),
    path('forgot_password/', views.forgot_password, name='auth_forgot_password'),
    path('reset_password/<uidb64>/<token>', views.reset_password, name='auth_reset_password'),
    path('reset_password/done/', auth_views.PasswordResetDoneView.as_view(template_name="reset_password/reset_password_done.html"), name="auth_reset_password_done"),
    path("reset/done/",auth_views.PasswordResetCompleteView.as_view(template_name="reset_password/reset_password_complete.html"), name="auth_reset_password_complete",),
    path("proctor/", views.proctor_management, name="proctor_management"),
    path('student', include('student_dashboard_proctor.urls')),
    path('faculty', include('faculty_dashboard_proctor.urls')),
    path('office', include('office_dashboard_proctor.urls')),
    path('attendence_management',views.atttendence_management,name="attendence_management"),
    path('attendence',include('Attendence_Management.urls')),
    path('notes_and_qp_mgmt', include('notes_and_qp_mgmt.urls'))
]
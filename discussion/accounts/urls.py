from django.urls import path 
from .views import SignUpView, EditSettingsView, ShowProfilePageView, EditUserPageView, CreateUserProfilePageView, PasswordsChangeView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("edit_settings/", EditSettingsView.as_view(), name="edit_settings"),
    path("password/", PasswordsChangeView.as_view(), name="password"),
    path("<int:pk>/user_profile/", ShowProfilePageView.as_view(), name="user_profile"),
    path("<int:pk>/edit_profile_page/", EditUserPageView.as_view(), name="edit_profile_page"),
    path("create_profile_page/", CreateUserProfilePageView.as_view(), name="create_user_profile_page"),
]

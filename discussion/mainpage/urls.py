from django.urls import path
from .models import Profile
from .views import HomePageView

urlpatterns = [
    path("profile/", Profile.as_view(), name="profile"),
    path("", HomePageView.as_view(), name="home"),
]

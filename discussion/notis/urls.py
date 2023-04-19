from django.urls import path
from .views import ShowNotifications, DeleteNotifications

urlpatterns = [
    path("<noti_id>/delete/", DeleteNotifications, name="delete_notifications"),
    path("show/", ShowNotifications, name="show_notifications"),
]

from django.db import models
from django.conf import settings
# from threads.models import Thread


# Create your models here.

NOTIFICATION_TYPES = ((1, "Like"), (2, "Comment"), (3, "Watch"))


class Notification(models.Model):
    thread = models.ForeignKey("threads.Thread", on_delete=models.CASCADE,
                               related_name="noti_post", blank=True, null=True)
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="noti_from_user")
    reciever = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="noti_to_user")
    notification_type = models.IntegerField(choices=NOTIFICATION_TYPES)
    text_preview = models.CharField(max_length=50, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    is_seen = models.BooleanField(default=False)
    reciever2 = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name="noti_to_other_user", blank=True, null=True)  # useless rn

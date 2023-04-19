from django.db import models
from django.conf import settings
from accounts.models import CustomUser


# Create your models here.

class Message(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="message_user",
    )
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="from_user",
    )
    recipient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="to_user",
    )
    body = models.TextField(max_length=1000, blank=True, null=True)
    date=models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False) #not really required i think
    
    def send_message(from_user, to_user, body):
        sender_message = Message(
            user = from_user,
            sender = from_user,
            recipient = to_user,
            body=body,
            is_read = True,
        )
        sender_message.save()
        
        recipient_message = Message(
            user = to_user,
            sender = from_user,
            recipient = from_user,
            body=body,
        )
        recipient_message.save()
        return sender_message
    
    def get_message(user):
        messages = Message.objects.filter(user=user).values("recipient").annotate(last=models.Max("date")).order_by("-last")
        users = [
            {
                "recipient": CustomUser.objects.get(pk=message["recipient"]),
                "last": message["last"],
                "unread":Message.objects.filter(user=user, recipient__pk=message["recipient"], is_read=False).count(),
            }
            for message in messages
        ]
        return users

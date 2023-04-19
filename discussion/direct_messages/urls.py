from django.urls import path
from .views import NewConversation, Message_inbox, Directs, SendMessages, LoadMore

urlpatterns = [
    path("your_messages/", Message_inbox, name="message_inbox"),
    path("new_conversation/<int:pk>",NewConversation, name="new_conversation"),
    path("directs/<int:pk>/", Directs, name="directs"),
    path("send/", SendMessages, name="send_messages"),
    path('loadmore/', LoadMore, name='loadmore'),
]

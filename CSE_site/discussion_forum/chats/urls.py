from django.urls import path
# from .views import ChatPage

# urlpatterns = [
#     path("", ChatPage.as_view(), name="livechat"),    
# ]

from .views import home, room, checkview, send, getMessages

urlpatterns = [
    path('', home, name='livechat'),
    path('<str:room>/', room, name='room'),
    path('checkview', checkview, name='checkview'),
    path('<str:room>/send', send, name='send'),
    path('getMessages/<str:room>/', getMessages, name='getMessages'),
]
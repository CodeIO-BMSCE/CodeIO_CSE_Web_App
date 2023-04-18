from django.urls import path
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("", ChatConsumer.as_asgi(),),
]

# from django.urls import path
# from .consumers import ChatConsumer

# websocket_urlpatterns = [
#     path("", ChatConsumer.as_asgi()),
#     ]


# from django.urls import path

# from . import consumers

# websocket_urlpatterns = [
#     path('ws/<str:room_name>/', ChatConsumer.as_asgi()),
# ]
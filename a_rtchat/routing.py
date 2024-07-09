from django.urls import path
from .consumers import *

websocket_urlpatterns = [
    path('ws/chatroom/<str:chatroom_name>/', ChatRoomConsumer.as_asgi()),
]

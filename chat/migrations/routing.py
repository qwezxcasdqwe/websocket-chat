from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("ws/chat/<srt:room_name>/", consumers.ChatConsumer.as_asgi()), #основной маршрутизатор для сокетов
]
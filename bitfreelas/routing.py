from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from channels.auth import AuthMiddlewareStack

from projects import consumers

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            path('ws/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
        ])
    ),
})

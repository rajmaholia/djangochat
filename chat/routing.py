from django.urls import path 
from .consumers import ChatConsumer

websocket_urlpatterns = [
    path('room/<str:id>/',ChatConsumer.as_asgi())
]
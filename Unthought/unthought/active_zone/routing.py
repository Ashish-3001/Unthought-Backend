from django.urls import re_path
from django.conf.urls import include, url

from . import consumers

websocket_urlpatterns = [
    url(r'ws/chat/(?P<room_name>[^/]+)/$', consumers.ChatRoomConsumer.as_asgi()),
]
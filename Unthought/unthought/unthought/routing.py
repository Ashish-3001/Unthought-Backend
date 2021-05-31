from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
import active_zone.routing



application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter(
            active_zone.routing.websocket_urlpatterns
        )
    ),
})

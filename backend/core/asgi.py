"""
ASGI config für lorchPro
Exposed als ``application`` für ASGI-Server
"""

import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.development')

# Django ASGI Application initialisieren
django_asgi_app = get_asgi_application()

# Import der WebSocket-Routen (wird später mit apps/chat erstellt)
# from apps.chat import routing

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    # WebSocket-Routing wird später hinzugefügt
    # 'websocket': AllowedHostsOriginValidator(
    #     AuthMiddlewareStack(
    #         URLRouter(routing.websocket_urlpatterns)
    #     )
    # ),
})


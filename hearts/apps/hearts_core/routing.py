"""
Hearts Channel routing config.
"""

from django.conf.urls import url

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from hearts_core.consumers import EchoConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url(r'^doc/(?P<document_id>[1-9])$', EchoConsumer),
        ])
    ),
})

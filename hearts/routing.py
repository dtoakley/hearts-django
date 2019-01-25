
from django.conf.urls import include, url
from django.contrib import admin

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from hearts_core.consumers import HeartsConsumer

application = ProtocolTypeRouter({
    'websocket': AuthMiddlewareStack(
        URLRouter([
            url('^doc/(?P<document_id>[^/]+)$', HeartsConsumer),
            url('api/', include('api.urls')),
            url('admin/', admin.site.urls),
        ])
    ),
})

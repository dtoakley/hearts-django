"""
Hearts Channel routing config.
"""
from channels.routing import ProtocolTypeRouter
from channels.auth import AuthMiddlewareStack
from .consumers import ws_connect, ws_receive, ws_disconnect

application = ProtocolTypeRouter({
    'websocket.connect': AuthMiddlewareStack(ws_connect),
    'websocket.receive': AuthMiddlewareStack(ws_receive),
    'websocket.disconnect': AuthMiddlewareStack(ws_disconnect),
})

from logging import getLogger

from asgiref.sync import async_to_sync
from channels.generic.websocket import JsonWebsocketConsumer

from hearts_core.utils import MessageHandler

logger = getLogger(__name__)


class HeartsConsumer(JsonWebsocketConsumer):

    def connect(self):
        async_to_sync(self.channel_layer.group_add)('hearts', self.channel_name)
        self.accept()
        logger.info('Channel session open: %s', self.channel_name)

    def receive_json(self, content, **kwargs):
        logger.info('Websocket message received: %s', content)
        try:
            document_id = self.scope['url_route']['kwargs']['document_id']
            username = content.get('user')['username']

            message_handler = MessageHandler(document_id, username)
            response_message = message_handler.handle_message(content)

            async_to_sync(self.channel_layer.group_send)(
                'hearts',
                {
                    'type': 'hearts.message',
                    'text': response_message,
                },
            )
        except Exception as e:
            logger.exception('Unable to process websocket message %s', content)
            return

    def hearts_message(self, event):
        logger.info('Sending Websocket message: %s', event)
        self.send_json(content=event.get('text'))

    def disconnect(self, close_code):
        logger.info('Channel session closed: %s', self.channel_name)
        async_to_sync(self.channel_layer.group_discard)('hearts', self.channel_name)

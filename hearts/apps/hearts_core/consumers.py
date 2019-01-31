import json
from logging import getLogger
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from channels.generic.websocket import AsyncWebsocketConsumer

from hearts_core.models import Document, Content, Vote
from hearts_core.constants import MessageTypes

logger = getLogger(__name__)


class HeartsConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        self.document_id = self.scope['url_route']['kwargs']['document_id']
        self.document_group_name = 'document_{}'.format(self.document_id)

        await self.channel_layer.group_add(
            self.document_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            document = get_object_or_404(Document, pk=self.document_id)
        except KeyError:
            logger.debug('Document does not exist')
            return

        try:
            user = get_object_or_404(User, username=text_data_json.get('user').get('username'))
            action = text_data_json.get('action')
            content_text = text_data_json.get('text')

            if text_data_json.get('contentId'):
                content = get_object_or_404(Content, pk=text_data_json.get('contentId'))
                user_already_voted_on_content = content.user_already_voted(user)
            else:
                content = None
                user_already_voted_on_content = False

            if action == MessageTypes.ADD_CONTENT:
                content = Content.objects.create(document=document, author=user, text=content_text)

            elif action == MessageTypes.EDIT_CONTENT:
                content.text = content_text
                content.save()

            elif action == MessageTypes.REMOVE_CONTENT:
                response = {
                    'contentDeletedId': content.id
                }
                content.delete()
                await self.send_response_message_to_group(response)
                return

            elif action == MessageTypes.REMOVE_VOTE and user_already_voted_on_content:
                content.votes.get(content=content, author=user).delete()
                content.save()

            elif action == MessageTypes.ADD_VOTE and not user_already_voted_on_content:
                content.votes.create(content=content, author=user)
                content.save()

            elif user_already_voted_on_content:
                logger.info('2nd vote attempted by user: %s', user.username)

        except (KeyError, ValueError, User.DoesNotExist, Content.DoesNotExist, Vote.DoesNotExist) as error:
            logger.debug('Unable to error process the websocket message: ', str(error))
            return

        await self.send_response_message_to_group(content.as_dict())

    async def send_response_message_to_group(self, response_message):
        await self.channel_layer.group_send(
            self.document_group_name,
            {
                'type': 'hearts_reply',
                'message': response_message
            }
        )

    async def hearts_reply(self, event):
        message = event.get('message')

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'text': message
        }))

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

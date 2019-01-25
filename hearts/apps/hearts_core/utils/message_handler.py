from logging import getLogger
from typing import Any, Dict

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from hearts_core.constants import MessageTypes
from hearts_core.models import Content, Document

logger = getLogger(__name__)


class MessageHandler:

    def __init__(self, document_id: int, username: str) -> None:
        self.document = get_object_or_404(Document, pk=document_id)
        self.user = get_object_or_404(User, username=username)

    def handle_message(self, message: Dict[str, Any]) -> Dict[str, Any]:
        message_type, message_text, content_id = self._parse_message(message)

        if message_type == MessageTypes.ADD_CONTENT:
            content = Content.objects.create(document=self.document, author=self.user, text=message_text)
        elif message_type == MessageTypes.EDIT_CONTENT:
            Content.objects.filter(pk=content_id).update(text=message_text)
            content = get_object_or_404(Content, pk=content_id)
        else:
            content = get_object_or_404(Content, pk=content_id)

        user_already_voted_on_content = content.user_already_voted(self.user)

        if message_type == MessageTypes.REMOVE_CONTENT:
            response_message = {'contentDeletedId': content.id}
            content.delete()
            return response_message

        elif message_type == MessageTypes.ADD_VOTE and not user_already_voted_on_content:
            content.votes.create(content=content, author=self.user)
            content.save()

        elif message_type == MessageTypes.REMOVE_VOTE and user_already_voted_on_content and content.votes.count() > 0:
            content.votes.get(content=content, author=self.user).delete()
            content.save()

        return content.as_dict()

    def _parse_message(self, message: Dict[str, Any]) -> [str, str, str]:
        message_type = message.get('action')
        message_text = message.get('text')
        content_id = message.get('contentId', None)

        return message_type, message_text, content_id

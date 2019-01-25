import json
from logging import getLogger
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from hearts_core.models import Document, Content, Vote
from hearts_core.constants import MessageTypes


logger = getLogger(__name__)


def ws_connect(message):
    try:
        prefix, document_id = message['path'].strip('/').split('/')
        if prefix != 'doc':
            logger.debug('invalid ws path=%s', message['path'])
            return
        doc = Document.objects.get(pk=document_id)
    except (ValueError, Document.DoesNotExist):
        logger.debug('invalid ws path=%s or document does not exist', message['path'])
        return

    message.reply_channel.send({"accept": True})
    Group('document-' + document_id).add(message.reply_channel)
    message.channel_session['document_id'] = str(doc.id)


def ws_receive(message):
    try:
        document_id = message.channel_session.get('document_id')
        doc = get_object_or_404(Document, pk=document_id)
    except KeyError:
        logger.debug('room does not exist')
        return

    try:
        message = json.loads(message.get('text'))
    except ValueError:
        logger.debug('ws content is not json text')
        return

    try:
        user = get_object_or_404(User, username=message.get('user')['username'])
        action = message.get('action')
        content = None
        user_already_voted_on_content = False
        message_text = message.get('text')

        if message.get('contentId'):
            content = get_object_or_404(Content, pk=message['contentId'])
            user_already_voted_on_content = content.user_already_voted(user)

        if action == MessageTypes.ADD_CONTENT:
            content = Content.objects.create(document=doc, author=user, text=message_text)

        elif action == MessageTypes.EDIT_CONTENT:
            content.text = message_text
            content.save()

        elif action == MessageTypes.REMOVE_CONTENT:
            response = {
                'contentDeletedId': content.id
            }
            content.delete()
            Group('document-' + document_id).send({'text': json.dumps(response)})
            return

        elif action == MessageTypes.REMOVE_VOTE and user_already_voted_on_content and content.votes.count() > 0:
            content.votes.get(content=content, author=user).delete()
            content.save()

        elif action == MessageTypes.ADD_VOTE and not user_already_voted_on_content:
            content.votes.create(content=content, author=user)
            content.save()

        elif user_already_voted_on_content:
            logger.info('2nd vote attempted by user: %s', user.username)

    except (KeyError, ValueError, User.DoesNotExist, Content.DoesNotExist, Vote.DoesNotExist) as error:
        logger.debug('Unable to error process the ws message: ', str(error))
        return
    Group('document-' + document_id).send({'text': json.dumps(content.as_dict())})


def ws_disconnect(message):
    document_id = message.channel_session['document_id']
    Group('document-' + document_id).discard(message.reply_channel)


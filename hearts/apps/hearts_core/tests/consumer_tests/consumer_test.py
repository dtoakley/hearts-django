from channels.tests import ChannelTestCase, HttpClient
from datetime import datetime
from django.contrib.auth.models import User

from hearts_core.models import Document


class TestConsumers(ChannelTestCase):

    def setUp(self):
        self.test_client = HttpClient()
        self.test_user = User.objects.create()
        self.test_document = Document.objects.create(title='test document', owner=self.test_user)
        self.test_new_content_data = {'id': None, 'author': self.test_user.username, 'text': 'test content', 'votes': 0}
        self.test_vote_data = {'id': 1, 'author': self.test_user.username, 'text': 'test content', 'votes': 0, 'action': 'add_vote'}
        self.test_client.login(username=self.test_user.username, password=self.test_user.password)
        self.test_client.send_and_consume('websocket.connect', path='/doc/1')

    def test_receive_and_create_document(self):
        # given
        expected_response = {'id': 1, 'document': 'test document', 'author': self.test_user.username,
                             'text': 'test content', 'votes': 0, 'created_on': datetime.today().strftime('%b %d, %Y')}

        # when
        self.test_client.send_and_consume("websocket.receive", text=self.test_new_content_data, path='/doc/1')

        # then
        self.assertEqual(self.test_client.receive(), expected_response)
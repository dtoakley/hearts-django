import pytest

from django.urls import reverse
from django.contrib.auth.models import User

from hearts_core.tests.helpers import create_test_document_with_time_offset


@pytest.mark.django_db(transaction=False)
class TestDocumentView(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_user = User.objects.create()

    def test_with_past_document(self, admin_client):
        # given
        past_doc = create_test_document_with_time_offset(self.test_user, 'past document', -5)
        url = reverse('document', args=(past_doc.id,))

        # when
        response = admin_client.get(url)

        # then
        assert response.status_code == 200
        assert b'past document' in response.content

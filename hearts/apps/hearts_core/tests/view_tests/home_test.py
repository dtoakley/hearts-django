
import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from hearts_core.tests.helpers import create_test_document_with_time_offset

from hearts_core.models import Document


@pytest.mark.django_db(transaction=False)
class TestHomeView(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_user = self.test_user = User.objects.create()
        self.test_past_document_1 = create_test_document_with_time_offset(self.test_user, 'past doc 1', -30)
        self.test_past_document_2 = create_test_document_with_time_offset(self.test_user, 'past doc 2', -5)
        self.test_future_document = create_test_document_with_time_offset(self.test_user, 'future doc', 30)

    def test_with_no_documents(self, client):

        # given
        Document.objects.all().delete()

        # when
        response = client.get(reverse('home'))

        # then
        assert response.status_code == 200
        assert b'No documents are available.' in response.content

    def test_returns_past_documents_only(self, client):

        # when
        response = client.get(reverse('home'))

        # then
        assert response.status_code == 200
        assert len(response.context['latest_document_list']) == 2
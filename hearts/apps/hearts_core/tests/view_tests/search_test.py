import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from hearts_core.models import Document


@pytest.mark.django_db(transaction=False)
class TestSearchView(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_user = User.objects.create()
        self.test_document_brainstorm = Document.objects.create(title='brainstorm document', owner=self.test_user)
        self.test_document_feedback = Document.objects.create(title='feedback document', owner=self.test_user)

    def test_search_single_match_returns_single_document(self, client):

        # when
        response = client.get(reverse('search'), {'query': 'brainstorm'})

        # then
        assert response.status_code == 200
        assert b'brainstorm document' in response.content
        assert b'feedback document'not in response.content

    def test_search_double_match_returns_two_documentss(self, client):

        # when
        response = client.get(reverse('search'), {'query': 'document'})

        # then
        assert response.status_code == 200
        assert b'brainstorm document' in response.content
        assert b'feedback document' in response.content

    def test_search_no_match_returns_no_documents(self, client):

        # when
        response = client.get(reverse('search'), {'query': 'test'})

        # then
        print(response.content)
        assert response.status_code == 200
        assert b'brainstorm document' not in response.content
        assert b'No documents found.' in response.content






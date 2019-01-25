from django.urls import reverse

import pytest

from django.contrib.auth.models import User


@pytest.mark.django_db(transaction=False)
class TestSearchView(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_user = User.objects.create()

    def test_create_redirects_to_document(self, admin_client):
        # when
        response = admin_client.post(reverse('create'), {'title': 'test document'})

        # then
        assert response.status_code == 302
        assert '/doc/' in response.url


from django.contrib.auth.models import User

import pytest

from hearts_core.models import Document


@pytest.fixture
def user():
    yield User.objects.create(username='test')


@pytest.fixture
def document(user):
    yield Document.objects.create(title='test_doc', owner=user)

import pytest

from django.contrib.auth.models import User

from hearts_core.tests.helpers import create_test_document_with_time_offset


@pytest.mark.django_db(transaction=False)
class TestDocument(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_user = User.objects.create()


    def test_was_created_recently_with_recent_document(self):
        # given
        recent_document = create_test_document_with_time_offset(self.test_user, 'test', -0.1)

        # when
        result = recent_document.was_created_recently()

        # then
        assert result is True

    def test_was_created_recently_with_future_document(self):
        # given
        future_document = create_test_document_with_time_offset(self.test_user, 'test', 30)

        # when
        result = future_document.was_created_recently()

        # then
        assert result is False

    def test_was_created_recently_with_old_document(self):
        # given
        old_document = create_test_document_with_time_offset(self.test_user, 'test', -30)

        # when
        result = old_document.was_created_recently()

        # then
        assert result is False



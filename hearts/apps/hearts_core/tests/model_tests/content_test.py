import pytest
from django.contrib.auth.models import User

from hearts_core.models import Document, Content, Vote


@pytest.mark.django_db(transaction=False)
class TestContent(object):

    @pytest.fixture(autouse=True)
    def setup(self):
        self.test_user = User.objects.create()
        self.test_doc = Document.objects.create(title='test', owner=self.test_user)
        self.test_content = Content.objects.create(document=self.test_doc, author=self.test_user, text='test text')
        self.test_vote = Vote.objects.create(content=self.test_content, author=self.test_user)

    def test_as_dict_returns_correctly(self):
        # given
        expected_dict = {'id': self.test_content.id,
                         'document': self.test_doc.title,
                         'author': self.test_content.author.username,
                         'text': self.test_content.text,
                         'votes': [self.test_vote.as_dict()],
                         'created_on': self.test_content.created_on.strftime('%b %d')}
        # when
        result = self.test_content.as_dict()

        # then
        assert result == expected_dict

    def test_user_already_voted_with_new_user(self):
        # given
        new_user = User.objects.create(username="new user")
        new_vote = Vote(content=self.test_content, author=new_user)

        # when
        result = self.test_content.user_already_voted(new_vote.author)

        # then
        assert result is False

    def test_user_already_voted_with_repeat_user(self):

        # when
        result = self.test_content.user_already_voted(self.test_vote.author)

        # then
        assert result is True




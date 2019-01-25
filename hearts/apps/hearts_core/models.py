import datetime

from django.db.models import Model, ForeignKey, DateTimeField, TextField, CharField, IntegerField, CASCADE
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.timesince import timesince

from ckeditor.fields import RichTextField


class Document(Model):
    title = CharField(max_length=100)
    owner = ForeignKey(User, on_delete=CASCADE)
    created_on = DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_on',)

    def __str__(self):
        return self.title

    def was_created_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.created_on <= now

    def as_dict(self):
        return {'id': self.id, 'owner': self.owner.username, 'title': self.title}

    was_created_recently.admin_order_field = 'created_on'
    was_created_recently.boolean = True
    was_created_recently.short_description = 'Created recently?'


class Content(Model):
    document = ForeignKey(Document, on_delete=CASCADE, related_name='contents')
    author = ForeignKey(User, on_delete=CASCADE, related_name='contents')
    text = RichTextField()
    created_on = DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

    def as_dict(self):
        return {'id': self.id, 'document': self.document.title, 'author': self.author.username,
                'text': self.text, 'votes': [vote.as_dict() for vote in self.votes.all()],
                'created_on': self.created_on.strftime('%b %d')
                }

    def user_already_voted(self, author):
        return self.votes.filter(author=author).exists()


class Vote(Model):
    content = ForeignKey(Content, on_delete=CASCADE, related_name='votes')
    author = ForeignKey(User, on_delete=CASCADE, related_name='votes')
    created_on = DateTimeField(auto_now_add=True)

    def as_dict(self):
        return {'id': self.id, 'author': self.author.username, 'created_on': self.created_on.strftime('%b %d, %Y')}

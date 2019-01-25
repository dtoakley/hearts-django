from django.contrib.auth.models import User

from rest_framework import serializers

from hearts_core.models import Content, Document, Vote


class DocumentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Document
        fields = ('id', 'title', 'owner', 'created_on')


class VoteSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Vote
        fields = ('id', 'author', 'created_on')


class ContentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    votes = VoteSerializer(many=True, read_only=True)
    created_on = serializers.DateTimeField(format="%b %d")

    class Meta:
        model = Content
        fields = ('id', 'document', 'author', 'text', 'votes', 'created_on')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)

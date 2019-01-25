from django.shortcuts import get_object_or_404
from rest_framework import viewsets, response, permissions
from rest_framework.generics import (CreateAPIView, GenericAPIView,
                                     ListCreateAPIView, RetrieveUpdateDestroyAPIView)

from .serializers import DocumentSerializer, ContentSerializer
from hearts_core.models import Document, Content
from django.contrib.auth.models import User

from .serializers import UserSerializer


class DocumentListView(ListCreateAPIView):
    serializer_class = DocumentSerializer
    queryset = Document.objects.all()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user, title=self.request.POST['title'])


class DocumentDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = DocumentSerializer
    lookup_url_kwarg = 'document_id'

    def get_object(self):
        return get_object_or_404(Document, pk=self.kwargs[self.lookup_url_kwarg])


class DocumentContentsView(ListCreateAPIView, RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'document_id'

    def get_queryset(self):
        document = get_object_or_404(Document, pk=self.kwargs[self.lookup_url_kwarg])
        return Content.objects.filter(document=document)

    def perform_create(self, serializer):
        document = get_object_or_404(Document, pk=self.request.POST['document'])
        serializer.save(document=document, author=self.request.user, text=self.request.POST['text'])


class ContentDetail(RetrieveUpdateDestroyAPIView):
    serializer_class = ContentSerializer
    lookup_url_kwarg = 'content_id'

    def get_object(self):
        return get_object_or_404(Content, pk=self.kwargs[self.lookup_url_kwarg])


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return response.Response(UserSerializer(request.user, context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)

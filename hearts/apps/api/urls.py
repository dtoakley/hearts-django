from django.conf.urls import include, url
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import DocumentListView, DocumentDetailView, DocumentContentsView, ContentDetail, UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls

urlpatterns += [
    url(r'^documents/?$', DocumentListView.as_view(), name='document_list'),
    url(r'^documents/(?P<document_id>[0-9]+)/?$', DocumentDetailView.as_view(), name='document_details'),
    url(r'^documents/(?P<document_id>[0-9]+)/contents/?$', DocumentContentsView.as_view(), name='document_contents_list'),
    url(r'^contents/(?P<content_id>[0-9]+)/?$', ContentDetail.as_view(), name='document_details'),
    url(r'^obtain-auth-token/?$', csrf_exempt(obtain_auth_token)),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
]

import datetime

from django.utils import timezone

from hearts_core.models import Document


def create_test_document_with_time_offset(user, title, days_offset):
    document = Document.objects.create(title=title, owner=user)
    new_time = timezone.now() + datetime.timedelta(days=days_offset)
    document.created_on = new_time
    document.save()
    return document

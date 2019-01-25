
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.db.utils import IntegrityError


class Command(BaseCommand):
    
    def handle(self, *args, **options):
        auth_model = get_user_model()
        try:
            new_user = auth_model.objects.create_superuser('admin', 'djangodevadmin@avaaz.org', 'abcd1234')
        except IntegrityError:
            print("'admin' user already exists")

from django.contrib.auth.models import User
from django.core.management import BaseCommand

from authors.models import Author


class Command(BaseCommand):

    def handle(self, *args, **options):
        user = User.objects.filter(username='name').first()
        if not user:
            User.objects.create_superuser(username='name', password='1', email='admin@mail.ru')
            data_author = {
                'first_name': 'Alex',
                'last_name': 'Pushkin',
                'birthday_year': 1789
            }
            author = Author.objects.create(**data_author)

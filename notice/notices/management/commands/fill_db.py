import json
from django.core.management.base import BaseCommand
from notices.models import User


def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        users = load_from_json('notices/fixtures/users.json')

        User.objects.all().delete()
        for user in users:
            usr = user.get('fields')
            usr['id'] = user.get('id')
            new_user = User(**usr)
            new_user.save()

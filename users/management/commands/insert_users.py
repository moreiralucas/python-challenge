"""Insert Users Management Command"""
import requests
from requests import Response
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from users.models import User
from users.utils import create_models_from_json, create_demo_user


class Command(BaseCommand):
    def handle(self, *args, **options):
        """Handle command"""
        url: str = "https://jsonplaceholder.typicode.com/users"
        try:
            with transaction.atomic():
                response: Response = requests.get(url=url, timeout=30)

                for data in response.json():
                    user: User = create_models_from_json(data)

                    self.stdout.write(
                        self.style.SUCCESS(
                            'Successfully inserted user "%s"' % user.name
                        ),
                    )
                    last_id = data["id"]
                create_demo_user(id=last_id + 1)
        except Exception as error:
            transaction.rollback()
            raise CommandError('Failed to insert users "%s"' % error)

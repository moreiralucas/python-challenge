"""Insert Users Management Command"""
import requests
from requests import Response
from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
from users.models import User, Address, Company, Localization

class Command(BaseCommand):

    def handle(self, *args, **options):
        """Handle command"""
        url: str = "https://jsonplaceholder.typicode.com/users"
        try:
            with transaction.atomic():
                response: Response = requests.get(url=url, timeout=30)

                for data in response.json():
                    localization: Localization = Localization(**data["address"]["geo"])
                    localization.save()
                    del data["address"]["geo"]

                    address: Address = Address.objects.create(
                        **data["address"],
                        localization=localization,
                    )

                    company: Company = Company.objects.create(
                        catchphrase=data["company"]["catchPhrase"],
                        name=data["company"]["name"],
                        bs=data["company"]["bs"],
                    )

                    del data["address"]
                    del data["company"]
                    user: User = User.objects.create(
                        **data,
                        address=address,
                        company=company,
                    )

                    self.stdout.write(
                        self.style.SUCCESS('Successfully inserted user "%s"' % user.name),
                    )
        except Exception as error:
            transaction.rollback()
            raise CommandError('Failed to insert users "%s"' % error)

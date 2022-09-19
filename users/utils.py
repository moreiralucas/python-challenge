"""Utils Module"""

from typing import Dict
from users.models import User, Address, Company, Localization


def create_models_from_json(data: Dict) -> User:
    """Create models of User, Address, Localization and Company from a json
    Sample of json
        {
            "id": 1,
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz",
            "address": {
                "street": "Kulas Light",
                "suite": "Apt. 556",
                "city": "Gwenborough",
                "zipcode": "92998-3874",
                "geo": {
                    "lat": "-37.3159",
                    "lng": "81.1496"
                }
            },
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": {
                "name": "Romaguera-Crona",
                "catchPhrase": "Multi-layered client-server neural-net",
                "bs": "harness real-time e-markets"
            }
        }
    """

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

    return user


def create_demo_user(user_id: int) -> User:
    """Create a demo User
    WARNING: Use this command only in development environment.
        Please, never use in production.
    """

    location: Dict = {"lat": "-71.4197", "lng": "71.7478"}
    address_data: Dict = {
        "street": "Norberto Crossing",
        "suite": "Apt. 950",
        "city": "South Christy",
        "zipcode": "23505-1337",
        "geo": location,
    }
    company: Dict = {
        "name": "Considine-Lockman",
        "catchPhrase": "Synchronised bottom-line interface",
        "bs": "e-enable innovative applications",
    }
    user_data: Dict = {
        "id": user_id,
        "name": "Demo User",
        "username": "demouser",
        "email": "demo@example.com",
        "address": address_data,
        "phone": "1-770-736-8031 x56442",
        "website": "https://example.com/",
        "company": company,
    }
    demo_user: User = create_models_from_json(user_data)
    demo_user.set_password("demo1234")
    demo_user.save()
    return demo_user

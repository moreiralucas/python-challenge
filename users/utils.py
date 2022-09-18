"""Utils Module"""

from typing import Dict, List
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

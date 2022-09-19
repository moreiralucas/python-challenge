"""BaseTest Module"""

from typing import Dict
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient, APITestCase
from rest_framework.authtoken.models import Token
from users.utils import create_models_from_json

User = get_user_model()


class BaseTest(APITestCase):
    """Base of all tests"""

    def setUp(self):
        """Method Docstring"""

        location: Dict = {"lat": "-37.3159", "lng": "81.1496"}
        address_data: Dict = {
            "street": "Kulas Light",
            "suite": "Apt. 556",
            "city": "Gwenborough",
            "zipcode": "92998-3874",
            "geo": location,
        }
        company: Dict = {
            "name": "Romaguera-Crona",
            "catchPhrase": "Multi-layered client-server neural-net",
            "bs": "harness real-time e-markets",
        }
        user_data: Dict = {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "sincere@april.biz",
            "address": address_data,
            "phone": "1-770-736-8031 x56442",
            "website": "hildegard.org",
            "company": company,
        }
        self.user_obj: User = create_models_from_json(user_data)
        self.user_obj.set_password("test1234")
        self.user_obj.save()

        self.client_unauthenticated = APIClient()
        self.client_user = APIClient()

        succes_login: bool = self.client_user.login(
            username=self.user_obj.username,
            password="test1234",
        )
        self.assertTrue(succes_login)

        # token: str = ""
        # if succes_login:
        #     _, token = Token.objects.get_or_create(user=self.user_obj)  # type: ignore
        self.client_user.force_authenticate(user=self.user_obj)

    def tearDown(self):
        """Method Docstring"""
        pass

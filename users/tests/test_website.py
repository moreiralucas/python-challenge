"""Test User Module"""
from typing import Dict
from users.tests.base import BaseTest
from rest_framework import status


class WebsiteTest(BaseTest):
    """Website Test class"""

    def test_list_websites(self):
        """Should test list websites"""

        url: str = "/users/websites/"
        response = self.client_user.get(
            path=url, content_type="application/json", format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json: Dict = response.json()
        self.assertTrue("websites" in response_json)
        self.assertIsInstance(response_json["websites"], list)
        self.assertEqual(response_json["websites"][0]["website"], "hildegard.org")

    def test_try_list_websites(self):
        """Should test that unauthenticated user cannot list websites"""

        url: str = "/users/websites/"
        response = self.client_unauthenticated.get(path=url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

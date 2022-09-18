"""Test User Module"""
from typing import Dict
from users.tests.base import BaseTest
from rest_framework import status


class UserTest(BaseTest):
    """Website Test class"""

    def test_list_users(self):
        """Should test create"""

        url: str = "/users/detail/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json: Dict = response.json()
        self.assertTrue("users" in response_json)
        self.assertIsInstance(response_json["users"], list)
        self.assertEqual(response_json["users"][0]["name"], "Leanne Graham")
        self.assertEqual(response_json["users"][0]["email"], "sincere@april.biz")
        self.assertEqual(response_json["users"][0]["company"], "Romaguera-Crona")

    def test_try_list_users(self):
        """Should test that unauthenticated user cannot list users"""

        url: str = "/users/detail/"
        response = self.client_unauthenticated.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_users(self):
        """Should test the search users endpoint"""
        url: str = "/users/"
        response = self.client.get(path=url, params={"name": "Romaguera-Crona"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_json: Dict = response.json()
        self.assertTrue("users" in response_json)
        self.assertIsInstance(response_json["users"], list)
        self.assertEqual(len(response_json["users"]), 1)
        self.assertEqual(response_json["users"][0]["name"], "Romaguera-Crona")
        self.assertIsInstance(response_json["users"][0]["id"], int)

    def test_try_search_users(self):
        """Should test unauthenticated user cannot search user"""
        url: str = "/users/"
        response = self.client_unauthenticated.get(path=url, params={"name": "Romaguera-Crona"})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_search_unexistent_user(self):
        """Should return a empty list when a user does not exists"""
        url: str = "/users/"
        response = self.client.get(path=url, params={"name": "Some Strange Name"})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_json: Dict = response.json()
        self.assertTrue("users" in response_json)
        self.assertIsInstance(response_json["users"], list)
        self.assertEqual(len(response_json["users"]), 0)

    def test_search_users_without_param(self):
        """Should return an bad request when the user name is not passed in query param"""
        url: str = "/users/"
        response = self.client.get(path=url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        response_json: Dict = response.json()
        self.assertTrue("detail" in response_json)
        self.assertIsInstance(response_json["detail"], "Required query param 'name'.")

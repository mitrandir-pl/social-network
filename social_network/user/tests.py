"""
Let's interact with the users.
Allows for user creation (registration)
User listing
    For testing purposes
Getting info on a specific user
Login/logout functionality
"""
import username as username
from django.test import TestCase
from django.urls import reverse
from rest_framework import status


from rest_framework.test import APITestCase

from .models import UserAPI


class UserTests(APITestCase):
    def setup_user_list(self):
        self.users = [
            {
                "username": "Paul",
                "email": "a@a.com",
                "role": "user"
            },
            {
                "username": "Alex",
                "email": "b@b.com",
                "role": "user"
            },
            {
                "username": "Steve",
                "email": "c@c.com",
                "role": "user"
            }
        ]
        for user in self.users:
            UserAPI.objects.create_user(**user).save()

    def test_list_users(self):
        """
        Send a request to get a usr list
        Expect to receive the same user list as in the DB
        """
        self.setup_user_list()  # database
        url = reverse('list_users')
        res = self.client.get(url)
        users = res.json()

        # Users have ids
        self.assertTrue(all(user.get('id') for user in users))

        # User list reflects DB table
        for user in users: user.pop('id')
        self.assertEqual(users, res.json())

    def test_register_user(self):
        """
        Register a new user
        Expecting that it returns as next fields:
        id, username, email, role
        """
        user = {
            "username": "Paul",
            "email": "a@a.com",
            "password": "123",
        }
        url = reverse('register')
        res = self.client.post(url, user, format='json')
        new_user = res.json()

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(new_user.pop('id'))
        self.assertTrue(new_user.pop('role'))

        user.pop('password')
        self.assertDictEqual(user, new_user)



class UserTest(TestCase):
    """
    Test case for UserAPI model

    Creating 3 test users
    Checking if they have required fields: username, email and role
    """

    @classmethod
    def setUpTestData(cls):
        test_user1 = UserAPI.objects.create_user(
            username="Paul", email="a@a.com", role="user"
        )
        test_user1.save()
        test_user2 = UserAPI.objects.create_user(
            username="Alex", email="b@b.com", role="user"
        )
        test_user2.save()
        test_user3 = UserAPI.objects.create_user(
            username="Steve", email="c@c.com", role="user"
        )
        test_user3.save()

    def test_user_fields(self):
        user1 = UserAPI.objects.get(id=1)
        user2 = UserAPI.objects.get(id=2)
        user3 = UserAPI.objects.get(id=3)
        username1 = f"{user1.username}"
        username2 = f"{user2.username}"
        username3 = f"{user3.username}"
        email1 = f"{user1.email}"
        email2 = f"{user2.email}"
        email3 = f"{user3.email}"
        role1 = f"{user1.role}"
        role2 = f"{user2.role}"
        role3 = f"{user3.role}"
        self.assertEqual(username1, "Paul")
        self.assertEqual(username2, "Alex")
        self.assertEqual(username3, "Steve")
        self.assertEqual(email1, "a@a.com")
        self.assertEqual(email2, "b@b.com")
        self.assertEqual(email3, "c@c.com")
        self.assertEqual(role1, "user")
        self.assertEqual(role2, "user")
        self.assertEqual(role3, "user")

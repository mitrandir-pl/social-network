"""
Let's interact with the users.
Allows for user creation (registration)
User listing
    For testing purposes
Getting info on a specific user by ID
Login/logout functionality
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import UserAPI


class UserFixtures:

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

    def setup_user_login(self):
        self.user = {
            "username": "rms",
            "email": "rms@gnu.org",
            "password": "qwerty12345"
        }
        UserAPI.objects.create_user(**self.user).save()


class UserTests(APITestCase, UserFixtures):
    def test_list_users(self):
        """
        Send a request to get a usr list
        Expect to receive the same user list as in the DB
        """
        self.setup_user_list()  # database
        url = reverse('list_users')
        response = self.client.get(url)
        users = response.json()

        # Users have ids
        self.assertTrue(all(user.pop('id') for user in users))

        # User list reflects DB table
        self.assertEqual(self.users, users)

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
        response = self.client.post(url, user, format='json')
        new_user = response.json()

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(new_user.pop('id'))
        self.assertTrue(new_user.pop('role'))

        user.pop('password')
        self.assertDictEqual(user, new_user)

    def test_get_user(self):
        """
        Get info on user by its ID
        """
        self.setup_user_list()
        url = reverse('get_user', kwargs={'pk': 1})
        response = self.client.get(url)
        user = response.json()

        # User have id
        self.assertTrue(user.pop('id'))

        self.assertDictEqual(self.users[0], user)

    def test_user_login(self):
        """
        Given an existing user account
        Expect to receive JWT token on a successful login
        """
        self.setup_user_login()
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            "username": self.user['username'],
            "password": self.user['password'],
        })
        self.assertEqual({'access', 'refresh'}, response.json().keys())

    def test_user_logout(self):
        """
        Given an exiting token that allows you
        to make requests on behalf of a particular user,
        Expect the token to be made expired on logout request
        """
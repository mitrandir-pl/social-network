from django.test import TestCase
from .models import UserAPI


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("HELOOOOOOOO!!!!!")
        test_user1 = UserAPI.objects.create_user(
            username="user1", email="a@a.com"
        )
        test_user1.save()
        test_user2 = UserAPI.objects.create_user(
            username="user2", email="b@b.com"
        )
        test_user2.save()

    def test_user_fields(self):
        user1 = UserAPI.objects.get(id=1)
        user2 = UserAPI.objects.get(id=2)
        username1 = f"{user1.username}"
        username2 = f"{user2.username}"
        email1 = f"{user1.email}"
        email2 = f"{user2.email}"
        self.assertEqual(username1, "user1")
        self.assertEqual(username2, "user2")
        self.assertEqual(email1, "a@a.com")
        self.assertEqual(email2, "b@b.com")

from django.test import TestCase
from .models import UserAPI


class UserTest(TestCase):

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

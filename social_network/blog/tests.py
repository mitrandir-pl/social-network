from django.test import TestCase
from .models import UserAPI, News


class UserTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user1 = UserAPI.objects.create_user(
            username="user1", email="a@a.com"
        )
        test_user1.save()

        test_user2 = UserAPI.objects.create_user(
            username="user2", email="b@b.com"
        )
        test_user2.save()

        test_news1 = News.objects.create(
            title="new title1",
            author=test_user1,
            content="this is the content!!!"
        )
        test_news1.save()

        test_news2 = News.objects.create(
            title="new title2",
            author=test_user2,
            content="this is more content!!!"
        )
        test_news2.save()

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

    def test_news(self):
        news1 = News.objects.get(id=1)
        news2 = News.objects.get(id=2)
        title1 = f"{news1.title}"
        title2 = f"{news2.title}"
        user1 = UserAPI.objects.get(id=1)
        user2 = UserAPI.objects.get(id=2)
        author1 = news1.author
        author2 = news2.author
        content1 = f"{news1.content}"
        content2 = f"{news2.content}"
        self.assertEqual(title1, "new title1")
        self.assertEqual(title2, "new title2")
        self.assertEqual(content1, "this is the content!!!")
        self.assertEqual(content2, "this is more content!!!")
        self.assertEqual(user1, author1)
        self.assertEqual(user2, author2)

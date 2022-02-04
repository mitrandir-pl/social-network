"""
Let's interact with the news.
Allows for news creation.
News listing
    For testing purposes
Getting info on a specific post by ID
Getting info on a specific news by author
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserAPI
from .models import News


class NewsFixtures:

    def setup_author(self):
        self.author = {
            "username": "rms",
            "email": "rms@gnu.org",
            "password": "qwerty12345"
        }
        UserAPI.objects.create_user(**self.author).save()

    def setup_news_list(self):
        author = UserAPI.objects.get(pk=1)
        self.news = [
            {
                'title': 'new title1',
                'author': author,
                'content': 'this is the content!!!'
            },
            {
                'title': 'new title2',
                'author': author,
                'content': 'this is more content!!!'
            },
            {
                'title': 'new title3',
                'author': author,
                'content': 'this is more content!!!'
            },
        ]
        for post in self.news:
            News.objects.create(**post).save()


class NewsTest(APITestCase, NewsFixtures):

    def setup_access_token(self):
        """
        Making a login to get an access token
        """
        self.setup_author()
        url = reverse('token_obtain_pair')
        response = self.client.post(url, {
            "username": self.author['username'],
            "password": self.author['password'],
        })
        self.access_token = response.json()['access']

    def test_list_news(self):
        """
        Send a request to get a news list
        Expect to receive the same news list as in the DB
        """
        self.setup_author()
        self.setup_news_list()
        url = reverse('news_list')
        response = self.client.get(url)
        news = response.json()

        # News have ids
        self.assertTrue(all(post.pop('id') for post in news))

        # News list reflects DB table
        self.assertEqual(self.news[0]['title'], news[0]['title'])
        self.assertEqual(self.news[0]['content'], news[0]['content'])

    def test_creation_post(self):
        """
        Creating a new post
        Expecting that it returns status201
        """
        self.setup_access_token()

        # Creating a post and making a request
        author = UserAPI.objects.get(pk=1)
        post = {
            'title': 'test',
            'author': author,
            'content': 'test',
        }
        url = reverse('create_post')
        response = self.client.post(
            url, post, HTTP_AUTHORIZATION=f'JWT {self.access_token}'
        )

        # Check if the status is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_post_by_id(self):
        """
        Get info on post by its ID
        """
        self.setup_author()
        self.setup_news_list()
        url = reverse('news_detail', kwargs={'pk': 1})
        response = self.client.get(url)
        post = response.json()

        # Post has id
        self.assertTrue(post.pop('id'))
        # Post has time fields
        self.assertTrue(post.pop('created'))

        self.assertEqual(self.news[0]['title'], post['title'])
        self.assertEqual(self.news[0]['content'], post['content'])

    def test_get_news_by_username(self):
        """
        Get posts by the author name
        """
        self.setup_access_token()
        self.setup_news_list()

        url = reverse('news_by_name')
        request_name = {'author': self.author['username']}
        response = self.client.post(
            url, request_name,
            HTTP_AUTHORIZATION=f'JWT {self.access_token}'
        )
        news = response.json()

        # Check if all user's news are returned
        self.assertEqual(len(news), 3)

        # Check if all posts have the same author
        author_name = self.author['username']
        self.assertTrue(
            all(author_name == post['author'] for post in news)
        )

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
        self.setup_author()
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

    def test_list_news(self):
        """
        Send a request to get a news list
        Expect to receive the same news list as in the DB
        """
        self.setup_news_list()  # database
        url = reverse('news_list')
        res = self.client.get(url)
        news = res.json()

        # News have ids
        self.assertTrue(all(post.pop('id') for post in news))

        # News list reflects DB table
        self.assertEqual(news, res.json())

    def test_creation_post(self):
        """
        Creating a new post
        Expecting that it returns status201
        """

        # Making a login to get an access token to create a post
        self.setup_author()
        url = reverse('token_obtain_pair')
        res = self.client.post(url, {
            "username": self.author['username'],
            "password": self.author['password'],
        })
        access_token = res.json()['access']

        # Creating a post and making a request
        author = UserAPI.objects.get(pk=1)
        post = {
            'title': 'test',
            'author': author,
            'content': 'test',
        }
        url = reverse('create_post')
        res = self.client.post(
            url,
            data=post,
            HTTP_AUTHORIZATION=f'JWT {access_token}'
        )

        # Check if the status is correct
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

    def test_get_post_by_id(self):
        """
        Get info on post by its ID
        """
        self.setup_news_list()
        url = reverse('news_detail', kwargs={'pk': 1})
        res = self.client.get(url)
        post = res.json()

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

        # Making a login to get an access token to create a post
        url = reverse('token_obtain_pair')
        self.setup_news_list()  # database
        res = self.client.post(url, {
            "username": self.author['username'],
            "password": self.author['password'],
        })
        access_token = res.json()['access']

        url = reverse('news_by_name')
        request_name = {'author': self.author['username']}
        res = self.client.post(url, request_name,
                               HTTP_AUTHORIZATION=f'JWT {access_token}')

        # Check if all user's news are returned
        self.assertEqual(len(res.json()), 3)

        # Check if all posts have the same author
        author_name = self.author['username']
        self.assertTrue(
            all(author_name == post['author'] for post in res.json())
        )

"""
Let's interact with the comments.
Allows for comment creation
Comment listing
    For testing purposes
Getting info on a specific comment by post title
"""
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from user.models import UserAPI
from blog.models import News
from .models import Comments


class CommentsFixtures:

    def setup_author(self):
        self.author = {
            "username": "rms",
            "email": "rms@gnu.org",
            "password": "qwerty12345"
        }
        UserAPI.objects.create_user(**self.author).save()

    def setup_post(self):
        author = UserAPI.objects.get(pk=1)
        self.post = {
            'title': 'new title1',
            'author': author,
            'content': 'this is the content!!!'
        }
        News.objects.create(**self.post).save()

    def setup_comments(self):
        author = UserAPI.objects.get(pk=1)
        post = News.objects.get(pk=1)
        self.comments = [
            {
                'post': post,
                'author': author,
                'content': 'test content',
            },
            {
                'post': post,
                'author': author,
                'content': 'another test content',
            }
        ]
        for comment in self.comments:
            Comments.objects.create(**comment).save()


class CommentsTest(APITestCase, CommentsFixtures):

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

    def test_list_comments(self):
        """
        Send a request to get a comments list
        Expect to receive the same comments list as in the DB
        """
        self.setup_author()
        self.setup_post()
        self.setup_comments()
        url = reverse('comments_list')
        response = self.client.get(url)
        comments = response.json()

        # Comments have ids
        self.assertTrue(all(comment.pop('id') for comment in comments))

        # Comments list reflects DB table
        self.assertEqual(
            [comment['content'] for comment in self.comments],
            [comment['content'] for comment in comments],
        )

    def test_creation_comment(self):
        """
        Creating a new comment
        Expecting that it returns status201
        """
        self.setup_access_token()
        self.setup_post()

        # Creating a comment and making a request
        author = UserAPI.objects.get(pk=1)
        post = News.objects.get(pk=1)
        comment = {
            'post': post,
            'author': author,
            'content': 'test',
        }
        url = reverse('create_comment')
        response = self.client.post(
            url, comment, HTTP_AUTHORIZATION=f'JWT {self.access_token}'
        )

        # Check if the status is correct
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_comments_by_title(self):
        """
        Get comments by the post title
        """
        self.setup_access_token()
        self.setup_post()
        self.setup_comments()
        url = reverse('comments_for_post')
        post_title = {'post': 'new title1'}
        response = self.client.post(
            url, post_title,
            HTTP_AUTHORIZATION=f'JWT {self.access_token}'
        )
        comments = response.json()

        # Check if all user's comments are returned
        self.assertEqual(len(comments), 2)

        # Check if all comments are from the same post
        post_title = self.post['title']
        self.assertTrue(
            all(post_title == comment['post'] for comment in comments)
        )

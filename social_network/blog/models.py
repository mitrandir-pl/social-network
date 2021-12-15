from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone


class UserAPI(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    TYPES_OF_USERS = [
        ('ADMIN', 'admin'),
        ('USER', 'user')
    ]
    role = models.CharField(
        max_length=100,
        choices=TYPES_OF_USERS,
        default='USER',
    )

    def __str__(self):
        return self.username


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(UserAPI, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserAPI, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.urls import reverse
from django.utils import timezone


class UserAPI(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(max_length=200, unique=True)
    password = models.CharField(max_length=100)
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

    def get_absolute_url(self):
        return reverse("get_user", kwargs={'pk': self.pk})

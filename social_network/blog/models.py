from django.db import models
from django.contrib.auth.models import User


class UserAPI(models.Model):
    nickname = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    role = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname

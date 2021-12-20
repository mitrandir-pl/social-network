from django.db import models
from user.models import UserAPI


class News(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(UserAPI, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

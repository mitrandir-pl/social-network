from django.db import models
from django.urls import reverse
from user.models import UserAPI


class News(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = models.ImageField(blank=True, null=True)
    author = models.ForeignKey(UserAPI, on_delete=models.CASCADE, to_field='username')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={'pk': self.pk})

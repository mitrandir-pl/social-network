from django.db import models
from user.models import UserAPI
from blog.models import News


class Comments(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(UserAPI, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return f"Comment by {self.author.username} on {self.post.title}"

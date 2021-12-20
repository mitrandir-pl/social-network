from rest_framework import serializers
from .models import Comments


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'post', 'author', 'content')
        model = Comments

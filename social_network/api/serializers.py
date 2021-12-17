from rest_framework import serializers
from user.models import UserAPI
from blog.models import News, Comments


class UserAPISerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'role')
        model = UserAPI


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'author', 'created', 'content')
        model = News


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'post', 'author', 'content')
        model = Comments

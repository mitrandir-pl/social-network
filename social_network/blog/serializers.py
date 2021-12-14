from rest_framework import serializers
from .models import UserAPI, News


class UserAPISerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'role')
        model = UserAPI


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'author', 'created', 'content')
        model = News

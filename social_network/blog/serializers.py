from rest_framework import serializers
from .models import News


class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'author', 'created', 'content')
        model = News

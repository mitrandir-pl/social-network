from rest_framework import serializers
from .models import UserAPI


class UserAPISerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'username', 'email', 'role')
        model = UserAPI

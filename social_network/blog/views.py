from rest_framework import generics
from .serializers import UserAPISerializer, NewsSerializer
from .models import UserAPI, News


class UserList(generics.ListAPIView):
    queryset = UserAPI.objects.all()
    serializer_class = UserAPISerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAPI.objects.all()
    serializer_class = UserAPISerializer


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

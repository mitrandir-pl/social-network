from rest_framework import generics
from .serializers import UserAPISerializer, NewsSerializer, CommentsSerializer
from .models import UserAPI, News, Comments


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


class CommentsList(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

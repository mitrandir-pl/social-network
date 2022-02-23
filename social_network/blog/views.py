from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewsSerializer
from .models import News


class NewsList(generics.ListAPIView):
    """
    Return news list.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveDestroyAPIView):
    """
    Return current post by  id.
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CreateNews(APIView):
    """
    Accepts title and content.
    Create a post.
    """

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)


class CurrentUserNews(APIView):
    """
    Accepts username and return all posts of this username.
    """

    def post(self, request):
        author = request.data['author']
        current_news = News.objects.filter(author=author)
        serializer = NewsSerializer(current_news, many=True)
        return Response(serializer.data)

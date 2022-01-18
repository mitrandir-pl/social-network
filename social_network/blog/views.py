import author as author
import current as current
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import NewsSerializer
from .models import News


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CreateNews(APIView):

    def post(self, request):
        serializer = NewsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)


class CurrentUserNews(APIView):

    def post(self, request):
        author = request.data['author']
        current_news = News.objects.filter(author=author)
        serializer = NewsSerializer(current_news, many=True)
        return Response(serializer.data)

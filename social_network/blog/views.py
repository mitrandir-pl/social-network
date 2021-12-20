from rest_framework import generics
from .serializers import NewsSerializer
from .models import News


class NewsList(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

from rest_framework import generics
from .serializers import CommentsSerializer
from .models import Comments


class CommentsList(generics.ListAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer

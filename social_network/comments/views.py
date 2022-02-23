from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import CommentsSerializer
from .models import Comments


class CommentsList(generics.ListAPIView):
    """
    Returns a comments list.
    """
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer


class CreateComment(APIView):
    """
    Accepts content and create a comment.
    """

    def post(self, request):
        serializer = CommentsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer:
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)


class CommentsForCurrentPost(APIView):
    """
    Accepts post name and returns comments for this post.
    """

    def post(self, request):
        post_ = request.data.get('post')
        current_comments = Comments.objects.filter(post=post_)
        serializer = CommentsSerializer(current_comments, many=True)
        return Response(serializer.data)

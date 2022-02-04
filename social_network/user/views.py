from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import UserAPI
from .serializers import UserAPISerializer


class UserList(generics.ListAPIView):
    queryset = UserAPI.objects.all()
    serializer_class = UserAPISerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAPI.objects.all()
    serializer_class = UserAPISerializer


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = ()

    def post(self, request):
        serializer = UserAPISerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)

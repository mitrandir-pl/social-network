import datetime

import jwt
from rest_framework import generics, status, permissions
from rest_framework.exceptions import AuthenticationFailed
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
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data)


class LoginView(APIView):

    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = UserAPI.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)
        response.data = {
            'jwt': token
        }

        return response


class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = UserAPI.objects.filter(id=payload['id']).first()
        serializer = UserAPISerializer(user)

        return Response(serializer.data)


class LogoutView(APIView):

    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response

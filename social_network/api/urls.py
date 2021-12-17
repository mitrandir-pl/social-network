from django.urls import path
from .views import UserList, UserDetail, NewsList, NewsDetail, CommentsList


urlpatterns = [
    path('users/', UserList.as_view()),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('news/', NewsList.as_view()),
    path('news/<int:pk>/', NewsDetail.as_view()),
    path('comments/', CommentsList.as_view())
]

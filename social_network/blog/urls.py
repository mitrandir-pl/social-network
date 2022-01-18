from django.urls import path

from .views import NewsList, NewsDetail, CurrentUserNews, CreateNews

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>/', NewsDetail.as_view()),
    path('my_news/', CurrentUserNews.as_view()),
    path('create/', CreateNews.as_view()),
]

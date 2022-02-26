from django.urls import path

from .views import NewsList, NewsDetail, CurrentUserNews, CreateNews, NewsEdit

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('<int:pk>/', NewsDetail.as_view(), name='news_detail'),
    path('my_news/', CurrentUserNews.as_view(), name='news_by_name'),
    path('create/', CreateNews.as_view(), name='create_post'),
    path('edit/<int:pk>/', NewsEdit.as_view(), name='news_edit')
]

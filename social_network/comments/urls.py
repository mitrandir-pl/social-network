from django.urls import path
from .views import CommentsList, CommentsForCurrentPost, CreateComment


urlpatterns = [
    path('', CommentsList.as_view()),
    path('curr_post/', CommentsForCurrentPost.as_view()),
    path('create/', CreateComment.as_view()),
]

from django.urls import path
from .views import CommentsList, CommentsForCurrentPost, CreateComment


urlpatterns = [
    path('', CommentsList.as_view(), name='comments_list'),
    path('curr_post/', CommentsForCurrentPost.as_view(), name='comments_for_post'),
    path('create/', CreateComment.as_view(), name='create_comment'),
]

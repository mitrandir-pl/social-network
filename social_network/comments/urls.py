from django.urls import path
from .views import CommentsList


urlpatterns = [
    path('', CommentsList.as_view())
]

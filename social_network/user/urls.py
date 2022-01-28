from django.urls import path

from .views import UserList, UserDetail, RegisterView


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('registration', RegisterView.as_view()),
]

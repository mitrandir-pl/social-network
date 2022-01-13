from django.urls import path

from .views import UserList, UserDetail, RegisterView, LoginView, LogoutView, UserView


urlpatterns = [
    path('', UserList.as_view()),
    path('<int:pk>/', UserDetail.as_view()),
    path('registration', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('userview', UserView.as_view()),
]

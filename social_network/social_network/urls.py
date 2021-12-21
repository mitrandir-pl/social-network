from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/users/', include('user.urls')),
    path('api/v1/news/', include('blog.urls')),
    path('api/v1/comments/', include('comments.urls')),
]

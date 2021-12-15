from django.contrib import admin
from .models import UserAPI, News, Comments


admin.site.register(UserAPI)
admin.site.register(News)
admin.site.register(Comments)

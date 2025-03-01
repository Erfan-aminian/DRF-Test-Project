
from django.contrib import admin
from django.urls import path, include
from api.views import user_profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_profile, name='user_profile'),
]

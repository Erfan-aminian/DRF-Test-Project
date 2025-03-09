
from django.contrib import admin
from django.urls import path, include
from api.views import user_profile, update_user_profile, delete_user_profile
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user_profile, name='user_profile'),
    path('user/<id>/', update_user_profile, name='update_user_profile'),
    path('user/del/<id>/', delete_user_profile, name='delete_user_profile'),
]

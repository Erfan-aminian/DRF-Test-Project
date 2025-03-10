
from django.contrib import admin
from django.urls import path, include
from api.views import UserProfileView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', UserProfileView.as_view(), name='user_profile'),
    path('user/<id>/', UserProfileView.as_view(), name='update_user_profile'),
]

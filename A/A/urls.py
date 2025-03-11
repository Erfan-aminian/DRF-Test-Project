
from django.contrib import admin
from django.urls import path, include
from api.views import UserProfileView, ListUserProfileView, CreateUserProfileView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/list/', ListUserProfileView.as_view(), name='user_profile_list'),
    path('user/create/', CreateUserProfileView.as_view(), name='user_profile_create'),
    path('user/', UserProfileView.as_view(), name='user_profile'),
    path('user/<id>/', UserProfileView.as_view(), name='update_user_profile'),
]

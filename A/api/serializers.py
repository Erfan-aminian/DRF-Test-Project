from rest_framework import serializers

from api.models import UserProfile


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'


class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('name', 'age','bio','email')



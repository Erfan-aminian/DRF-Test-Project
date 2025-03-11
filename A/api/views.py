from django.shortcuts import render
from rest_framework.response import Response
from .serializers import UserProfileSerializer, CreateUserSerializer
from .models import UserProfile
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView

# Create your views here.
class ListUserProfileView(ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

class CreateUserProfileView(CreateAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = CreateUserSerializer
class UserProfileView(APIView):
    def get(self, request):
        all_user_profile_obj = UserProfile.objects.all()
        serializer = UserProfileSerializer(instance=all_user_profile_obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def put(self, request, id):
        user_profile_obj = UserProfile.objects.get(id=id)
        serializer = UserProfileSerializer(instance=user_profile_obj, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, id):
        user_profile_obj = UserProfile.objects.get(id=id)
        user_profile_obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






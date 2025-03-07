from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response,
from .serializers import UserProfileSerializer, CreateUserSerializer
from .models import UserProfile

# Create your views here.
@api_view(['GET', 'POST'])
def user_profile(request):
    if request.method == 'GET':
        data = UserProfile.objects.all()
        serializer_data = UserProfileSerializer(instance= data, many=True)
        return Response(serializer_data.data)


    if request.method == 'POST':
        req_data = request.data
        serializer = CreateUserSerializer(data=req_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)





from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

class UserRegistrationView(generics.CreateAPIView):
    serializer_class=UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    pass   

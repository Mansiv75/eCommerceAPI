from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Product
from .serializers import ProductSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class=UserSerializer

class CustomTokenObtainPairView(TokenObtainPairView):
    pass   

#list all products and create a new one
class ProductListCreateView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

#retrieve a single product
class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


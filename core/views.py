from django.shortcuts import render
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Product
from .serializers import ProductSerializer
from .models import CartItem
from .models import Cart
from .serializers import CartItemSerializer, CartSerializer
from rest_framework import status
from rest_framework.response import Response

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


class CartView(generics.ListCreateAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Cart.objects.all()
    serializer_class=CartSerializer

class CartItemDeleteView(generics.DestroyAPIView):
    queryset=CartItem.objects.all()
    serializer_class=CartItemSerializer

    def delete(self, request, *args, **kwargs):
        cart_item=self.get_object()
        cart_item.delete()
        return Response({"message":"Item removed from cart"},status=status.HTTP_204_NO_CONTENT)
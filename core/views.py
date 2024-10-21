from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import UserSerializer, ProductSerializer, CartSerializer, CartItemSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import Product, CartItem, Cart
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
import stripe
from django.conf import settings
from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_SECRET_KEY
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

class ProductListCreateView(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filter_backends=[DjangoFilterBackend, filters.SearchFilter]
    search_fields=['name', 'description']    


class CheckoutView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            #get cart details
            cart_id=request.data.get('cart_id')
            cart=Cart.objects.get(id=cart_id)
            total_amount=sum([item.product.price * item.quantity for item in cart.items.all()])

            #create a stripe payment intent
            intent= stripe.PaymentIntent.create(
                amount= int(total_amount*100),
                currency= 'usd',
                payment_method_types=['card'],
            )

            return Response({
                'client_secret':intent['client_secret'],
                'amount': total_amount
            })
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
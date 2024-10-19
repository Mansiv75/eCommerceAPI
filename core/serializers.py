from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Product
from .models import CartItem
from .models import Cart
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["id", "username", "email", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user= User(**validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields="__all__"    


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        exclude=['cart']

class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'items')

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        cart = Cart.objects.create(**validated_data)
        for item_data in items_data:
            CartItem.objects.create(cart=cart, **item_data)
        return cart
    


from rest_framework import serializers
from apps.carrito_compras.models import Cart, Order
from apps.productos.serializers import ProductSerializer


class CartSerializer(serializers.ModelSerializer):
    producto = ProductSerializer()

    class Meta:
        model = Cart
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    cart = CartSerializer()

    class Meta:
        model = Order
        fields = '__all__'
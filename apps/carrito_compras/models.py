from django.db import models
from django.contrib.auth.models import User
from apps.productos.models import Product

class Cart(models.Model):
    producto = models.ForeignKey(Product, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

class Order(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='carts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')

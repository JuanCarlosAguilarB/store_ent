from django.urls import path
from .views import *

urlpatterns = [
    path('cart/', Cart.as_view(), name='cart'),
    # path('order/', Order.as_view(), name='oder')
]
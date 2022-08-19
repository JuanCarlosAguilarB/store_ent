from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import *
from .models import Cart, Order
from .pagination import *

class Cart(APIView):
    def get(self, request, format=None):
        if Cart.objects.all().exists():
            cart = Cart.objects.all()
            cart_serializer = CartSerializer(cart, many=True)
            
            results = paginator.paginate_queryset(cart, request)
            serializer = ProductSerializer(results, many=True)

            return paginator.get_paginated_response({'cart': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No cart found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    
    def post(self, request, *args, **kwargs):
        serializer = ProductSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



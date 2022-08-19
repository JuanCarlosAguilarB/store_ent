from django.shortcuts import render, get_object_or_404
from apps.categorias.models import Categoria

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from django.db.models.query_utils import Q

from .models import Product
from .serializers import *
from .pagination import SmallSetPagination, MediumSetPagination, LargeSetPagination


class ProductListView(APIView):
    def get(self, request, format=None):
        if Product.productobjects.all().exists():

            products = Product.productobjects.all()

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(products, request)
            serializer = ProductSerializer(results, many=True)

            return paginator.get_paginated_response({'products': serializer.data})
        else:
            return Response({'error': 'No products found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductListCategoryView(APIView):
    def get(self, request, category_id, format=None):
        if Product.Productobjects.all().exists():
            
            categoria = Categoria.objects.get(id=category_id)
            products = Product.postobjects.all().filter(categoria=categoria)

            paginator = SmallSetPagination()
            results = paginator.paginate_queryset(products, request)
            serializer = ProductSerializer(results, many=True)

            return paginator.get_paginated_response({'products': serializer.data})
        else:
            return Response({'error': 'No products found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ProductDetailView(APIView):
    def get(self, request, product_slug,format=None):
        products = get_object_or_404(Product, slug=product_slug)
        serializer = ProductSerializer(products)
        return Response({'products':serializer.data}, status=status.HTTP_200_OK)


class SearchProductView(APIView):

    def get(self,request,search_term):
        matches = Products.Productsobjects.filter(
            Q(nombre__icontains=search_term) |
            Q(descripcion__icontains=search_term) |
            Q(categoria__nombre__icontains=search_term)
        )

        paginator = MediumSetPagination()
        # results = paginator.paginate_queryset(matches, request)
        serializer = ProductsSerializer(matches, many=True)
        return Response({'filtered_productss':serializer.data},status=status.HTTP_200_OK)
    
    
    
    
    

class ProductCreateApiView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    
    serializer_class = ProductSerializer
    
    def post(self, request, *args, **kwargs):

        data = {
            'nombre' : request.data.get('nombre'), 
            'slug' : request.data.get('slug'), 
            'imagen' : request.data.get('imagen'), 
            'video' : request.data.get('video'), 
            'descripcion' : request.data.get('descripcion'), 
            'categoria' : request.data.get('categoria'), 
            'published' : request.data.get(''), 
            'precio' : request.data.get('precio'), 
            'cantidad' : request.data.get('cantidad')
            
        }
        serializer = ProductSerializerCreate(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

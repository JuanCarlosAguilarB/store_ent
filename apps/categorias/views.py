from apps.categorias.serializers import CategoriaSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Categoria
from rest_framework.pagination import PageNumberPagination


class ListCategoriasView(APIView):
    def get(self, request, format=None):
        if Categoria.objects.all().exists():
            categorias = Categoria.objects.all()

            result = []

            for categoria in categorias:
                if not categoria.parent:
                    item = {}
                    item['id'] = categoria.id
                    item['nombre'] = categoria.nombre
                    item['immagen'] = categoria.imagen.url

                    item['sub_categorias'] = []

                    for cat in categorias:
                        sub_item = {}
                        if cat.parent and cat.parent.id == category.id:
                            sub_item['id'] = cat.id
                            sub_item['nombre'] = cat.nombre
                            sub_item['imagen'] = cat.imagen.url

                            item['sub_categorias'].append(sub_item)

                    result.append(item)
                    
            return Response({'categorias': result}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No categories found'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
# Create your views here.

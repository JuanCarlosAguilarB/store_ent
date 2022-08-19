from rest_framework import serializers
from .models import Product
from apps.categorias.serializers import CategoriaSerializer

class ProductSerializer(serializers.ModelSerializer):
    imagen=serializers.CharField(source='get_imagen',allow_blank=True)
    video=serializers.CharField(source='get_video',allow_blank=True)
    # categoria=CategoriaSerializer(required=False, allow_null=True)
    class Meta:
        model=Product
        fields=[
            'nombre',
            'slug',
            'imagen',
            'video',
            'descripcion',
            'categoria',
            'published',
            'status',
            'precio',
            'cantidad',
        ]
        
class ProductSerializerCreate(serializers.ModelSerializer):
    # imagen=serializers.CharField(source='get_imagen',allow_blank=True)
    # video=serializers.CharField(source='get_video',allow_blank=True)
    # categoria=CategoriaSerializer(required=False, allow_null=True)
    class Meta:
        model=Product
        fields=[
            'nombre',
            'slug',
            'imagen',
            'video',
            'descripcion',
            'categoria',
            'published',
            'status',
            'precio',
            'cantidad',
        ]
        
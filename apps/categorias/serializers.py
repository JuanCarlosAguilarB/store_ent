from .models import *
from rest_framework import serializers

class CategoriaSerializer(serializers.ModelSerializer):
    imagen=serializers.CharField(source='get_imagen')
    class Meta:
        model=Categoria
        fields=[
            'id',
            'nombre',
            'imagen',
        ]
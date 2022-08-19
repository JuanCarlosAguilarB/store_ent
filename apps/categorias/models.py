from django.db import models

# Create your models here.
class Categoria(models.Model):
    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    parent = models.ForeignKey(
        'self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    
    nombre = models.CharField(max_length=255, unique=True)
    imagen =         models.ImageField(upload_to='media/categoria/')

    def __str__(self):
        return self.name

    def get_imagen(self):
        if self.imagen:
            return self.imagen.url
        return ''
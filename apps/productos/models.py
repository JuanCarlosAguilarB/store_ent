from django.db import models
from django.utils import timezone
from apps.categorias.models import Categoria
# Create your models here.


def product_directory_path(instance, filename):
    return 'producto/{0}/{1}'.format(instance.nombre, filename)



class Product(models.Model):

    class ProductObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    nombre =            models.CharField(max_length=255)
    slug =              models.SlugField(unique=True)
    imagen =            models.ImageField(upload_to=product_directory_path, blank=True, null=True)
    video =             models.FileField(upload_to=product_directory_path, blank=True, null=True)
    descripcion =       models.TextField()
    precio  =           models.IntegerField()
    cantidad =          models.IntegerField()

    # author =            models.CharField(max_length=255)
    categoria =          models.ForeignKey(Categoria, on_delete=models.PROTECT,blank=True, null=True)


    published =         models.DateTimeField(default=timezone.now)

    status =            models.CharField(max_length=10, choices=options, default='draft')

    objects =           models.Manager()  # default manager
    productobjects =    ProductObjects()  # custom manager

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.nombre

    def get_video(self):
        if self.video:
            return self.video.url
        return ''

    def get_imagen(self):
        if self.imagen:
            return self.imagen.url
        return ''
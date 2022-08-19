from django.urls import path

from .views import *


urlpatterns = [
    path('categorias', ListCategoriasView.as_view()),
]
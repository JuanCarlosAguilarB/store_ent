from django.urls import path

from .views import *


urlpatterns = [
    path('', ProductListView.as_view()),
    path('categoria/<categoria_id>', ProductListCategoryView.as_view()),
    path('<product_slug>', ProductDetailView.as_view()),
    path("search/<str:search_term>",SearchProductView.as_view()),
    path("crear/",ProductCreateApiView.as_view()),
    
]


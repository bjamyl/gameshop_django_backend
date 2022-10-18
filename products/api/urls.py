from django.urls import path
from .views import ProductsView, ProductDetail


urlpatterns = [
    path('products/', ProductsView.as_view(), name='all-products'),
    path('products/<int:pk>', ProductDetail.as_view(), name='product-detail'),
]

from django.urls import path
from .views import ProductsView, ProductDetail,SingleProduct


urlpatterns = [
    path('products/', ProductsView.as_view(), name='all-products'),
    # path('products/<int:pk>', ProductDetail.as_view(), name='product-detail'),
    path('products/<pk>', SingleProduct.as_view(), name='product-detail'),
    # path('products/<int:pk>', Product.as_view(), name='product-detail'),
]

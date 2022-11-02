from django.http import Http404
from .serializers import ProductSerializer
from rest_framework.views import APIView
from products.models import Product
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class ProductsView(generics.ListAPIView):
    #registering the serializer
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'description', 'category', 'product_type']
    
    #Defining 'GET' request for all products
    def get_queryset(self):
        return Product.objects.all()
    
# Getting a single product
class ProductDetail(APIView):
    def get(self,request,pk):
        try:
            product=Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
# class Product(generics.ListAPIView):
#     serializer_class = ProductSerializer
    
#     def get_queryset(self, pk):
#         return Product.objects.get(pk=pk)

class SingleProduct(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
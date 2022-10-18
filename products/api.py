# view api 

'''
    django 
        - function 
        - class based
        - generic based
        

    rest 
        - function                  *
        - class based               
        - generic based             *
        - viewsets   -----> class [CRUD]    *


'''
from math import prod
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.decorators import api_view
import django_filters.rest_framework
from rest_framework.permissions import IsAuthenticated 
from .serializers import ProductSerializer , BrandSerializer , CategorySerializer , BrandSerializerDetail,CategorySerializerDetail,ProductSerializerDetail
from .pagination import MyPagination
from .filters import ProductFilter
from .models import Product , Category , Brand



class ProductListAPI(generics.ListAPIView):
    serializer_class = ProductSerializer
    # queryset = Product.objects.filter(name__endswith='fox')
    queryset = Product.objects.all()
    pagination_class = MyPagination
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['name']
    filterset_class = ProductFilter
    permission_classes = [IsAuthenticated]
    
    
class ProductDetailAPI(generics.RetrieveAPIView):
    serializer_class = ProductSerializerDetail
    queryset = Product.objects.all()
    
    # product reviews 
    

class CategoryListAPI(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()



class CategoryDetailAPI(generics.RetrieveAPIView):
    serializer_class = CategorySerializerDetail
    queryset = Category.objects.all()
    
    # detail products




class BrandListAPI(generics.ListAPIView):
    serializer_class = BrandSerializer
    queryset = Brand.objects.all()


class BrandDetailAPI(generics.RetrieveAPIView):
    serializer_class = BrandSerializerDetail
    queryset = Brand.objects.all()
    
    # detail products

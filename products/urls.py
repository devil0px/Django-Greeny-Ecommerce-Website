from django.urls import  path
from .views import ProductList,ProductDetail,CategoryLíst,BrandLíst

app_name='products'

urlpatterns=[
    path('',ProductList.as_view(),name='product_list'),
    path('category/',CategoryLíst.as_view(),name='category_list'),
    path('brand/',BrandLíst.as_view(),name='brand_list'),
    path('<slug:slug>',ProductDetail.as_view(),name='product_detail'),
]
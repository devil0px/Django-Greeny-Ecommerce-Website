from django.urls import path 
from .views import ProductList,ProductDetail,CategoryList,BrandList,BrandDetail,product_list,CategoryDetail,add_to_favourites,add_review
from .api import  ProductListAPI,ProductDetailAPI,CategoryListAPI,CategoryDetailAPI,BrandListAPI,BrandDetailAPI 


app_name='products'




urlpatterns = [
    path('' , ProductList.as_view() , name='product_list'),
    path('add_to_wish' , add_to_favourites , name='add_to_favourites'),
    path('test' , product_list ),
    path('<slug:slug>' , ProductDetail.as_view() , name='product_detail'),
    path('<slug:slug>/review-add' , add_review , name='add_review'),
    path('category/' , CategoryList.as_view() , name='category_list'),
    path('category/<slug:slug>' , CategoryDetail.as_view() , name='category_detail'),
    path('brand/' , BrandList.as_view() , name='brand_list'),
    path('brand/<slug:slug>' , BrandDetail.as_view() , name='brand_detail'),
    
    
    # api url
    path('api/' , ProductListAPI.as_view()),
    path('api/<int:pk>' , ProductDetailAPI.as_view(),name='product_detail2'),
    path('api/brands' , BrandListAPI.as_view()),
    path('api/brands/<int:pk>' , BrandDetailAPI.as_view()),
    path('api/category' , CategoryListAPI.as_view()),
    path('api/category/<int:pk>' , CategoryDetailAPI.as_view()),   


]

from django.urls import path 
from .views import order_list , add_to_cart

app_name = 'orders'


urlpatterns = [
    path('' , order_list,name='order_list'),
    path('cart/add' , add_to_cart , name='add_to_cart')
]

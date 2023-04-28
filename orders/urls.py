from django.urls import path 
from .views import order_list , add_to_cart, checkout_page


from .api import OrderListAPI

app_name = 'orders'


urlpatterns = [
    path('' , order_list,name='order_list'),
    path('checkout' , checkout_page,name='checkout_page'),
    path('cart/add' , add_to_cart , name='add_to_cart'),
    
    
    
    # api 
    path('api' , OrderListAPI.as_view()),
    
]

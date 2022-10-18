from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Order , OrderDetail , CartOrder , CartOrderDetail



admin.site.register(Order) 
admin.site.register(OrderDetail) 
admin.site.register(CartOrder) 
admin.site.register(CartOrderDetail) 
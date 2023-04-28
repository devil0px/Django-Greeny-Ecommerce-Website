from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Order , OrderDetail , CartOrder , CartOrderDetail, Coupon


admin.site.register(Order) 
admin.site.register(OrderDetail) 
admin.site.register(CartOrder) 
admin.site.register(CartOrderDetail) 


class CoupnAmdin(admin.ModelAdmin):
    list_display = ['code','from_date','to_date','quantity','is_valid']

admin.site.register(Coupon,CoupnAmdin)
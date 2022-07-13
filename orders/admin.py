from django.contrib import admin

from .models import Order, Order_Details
admin.site.register(Order)
admin.site.register(Order_Details)

# Register your models here.

from django.db import models
import random
from django.utils import timezone
from django.utils.translation import gettext as _
from products.models import Product
from utils.generate_code import generaste_code
from django.contrib.auth.models import User

# Create your models here.

STATUS_CHOICES = (
    ('Inprogress','Inprogress'),
    ('Completed','Completed'),

)



class CartOrder(models.Model):
    user = models.ForeignKey(User,related_name='user_cart',on_delete=models.SET_NULL , null=True,blank=True)
    code = models.CharField(_("Code"),max_length=8 ,default=generaste_code)
    order_status = models.CharField(_("Order Status"),max_length=10 ,choices=STATUS_CHOICES)
    
    def __str__(self):
        return self.code
    
    
    def get_total(self):
        total = 0
        cart_detail = self.cart_detail.all()
        for product in cart_detail:
            total += product.total
        return total
    
    
class CartOrderDetail(models.Model):
    order = models.ForeignKey(CartOrder, verbose_name=_("order_detail"),related_name='cart_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name=_("Product"),related_name='cart_product' ,on_delete=models.SET_NULL , null=True , blank=True)
    quantity = models.FloatField(default=0)
    price = models.FloatField(default=0)
    total =  models.FloatField(default=0)
    
    def __str__(self):
        return str(self.order)






STATUS_CHOICES = (
    # ('Inprogress','Inprogress'),
    ('Recieved','Recieved'),
    ('Processed','Processed'),
    ('Shipped','Shipped'),
    ('Delivered','Delivered'),
)



class Order(models.Model):
    user = models.ForeignKey(User,related_name='user_orders',on_delete=models.SET_NULL , null=True,blank=True)
    code = models.CharField(_("Code"),max_length=8 ,default=generaste_code)
    order_status = models.CharField(_("Order Status"),max_length=10 ,choices=STATUS_CHOICES)
    order_time = models.DateTimeField(_("Order time"),default=timezone.now)
    delivery_time = models.DateTimeField(_("Delivery time"),null=True , blank=True)
    
    def __str__(self):
        return self.code
    
    
class OrderDetail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("order_detail"),related_name='order_detail', on_delete=models.CASCADE)
    product = models.ForeignKey(Product,verbose_name=_("Product"),related_name='order_product' ,on_delete=models.SET_NULL , null=True , blank=True)
    quantity = models.FloatField(_("Quanitity"))
    price = models.FloatField(_("price"))
    
    def __str__(self):
        return str(self.order)
    
    
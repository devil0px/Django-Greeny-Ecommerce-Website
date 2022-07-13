from django.db import models
import random
from django.utils.translation import gettext as _
from django.utils import timezone
from products.models import Product
# Create your models here.

def generate_code(length=8):
    numbers='123456789'
    return ''.join(random.choice(numbers) for _ in range(length))
STATUS_CHOICES=(
('Recieved','Recieved'),
('Processed','Processed'),
('Shipped','Shipped'),
('Delivered','Delivered'),

)

class Order(models.Model):
    code =models.CharField(_("Code") ,max_length=8,default=generate_code)
    order_status=models.CharField(_("OrderStatus") ,max_length=10,choices=STATUS_CHOICES)
    order_time =models.DateTimeField(_("OrderTime") ,default=timezone.now)
    delivery_time=models.DateTimeField(_("DeliveryTime") ,null=True,blank=True)

def __str__(self):
        return self.code




class  Order_Details(models.Model):
    order= models.ForeignKey(Order,verbose_name=_("Order_details"),related_name='order_details',on_delete=models.CASCADE)
    product= models.ForeignKey(Product,verbose_name=_("Product"),related_name='order_product',on_delete=models.SET_NULL,null=True,blank=True)
    quantity= models.FloatField()
    price= models.FloatField()


    def __str__(self):
        return str (self.order)
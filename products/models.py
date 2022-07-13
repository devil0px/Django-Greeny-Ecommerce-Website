
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

FLAG_TYPE = (

    ('new','new' ),
    ('feature','feature' ),

)

class Product(models.Model):
    name = models.CharField(_("Name") ,max_length=100)
    sku = models.IntegerField(_("Sku"))
    brand = models.ForeignKey('Brand',verbose_name=_("Prand"),related_name='produc_Prand',on_delete=models.SET_NULL ,null=True,blank=True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(max_length=10000)
    tags = ''
    flag = models.CharField(max_length=10,choices=FLAG_TYPE)
    category =models.ForeignKey('Category',verbose_name=_("Category"),related_name='produc_Category',on_delete=models.SET_NULL ,null=True,blank=True)

    def __str__(self):
        return self.name

class ProductImages (models.Model):
    product =models.ForeignKey(Product,verbose_name=_("Product"),related_name='Product_Image',on_delete=models.CASCADE)
    image  =models.ImageField(_("Image"),upload_to='product/')
    def __str__(self):
        return str(self.Product)


class Brand (models.Model):
    name = models.CharField(_("Name") ,max_length=50)

    def __str__(self):
        return self.name


class Category (models.Model):
    name = models.CharField(_("Name") ,max_length=100)
    image = models.ImageField(_("Image") ,upload_to='Category/')

    def __str__(self):
        return self.name


class Reviews (models.Model):
    user =models.ForeignKey(User,verbose_name=_("User"),related_name='review_author',on_delete=models.SET_NULL,null=True,blank=True)
    product =models.ForeignKey(Product,verbose_name=_("Product"),related_name='product_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(_("Review"),max_length=500)
    rate =models.IntegerField(_("Rate"),validators=[MinValueValidator(0),MaxValueValidator(5)])
    create_at = models.DateTimeField(_("Create_at"),default=timezone.now)

    def __str__(self):
        return f"{self.user.username}-{self.product.name}"
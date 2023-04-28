from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from taggit.managers import TaggableManager
from django.urls import reverse
from django.db.models.aggregates import Avg


FLAG_TYPE = (
    ('New' , 'New'),
    ('Feature' , 'Feature'),
)



class ProductQuerset(models.QuerySet):
    def price_greater_than(self,price):
        return self.filter(price__gt=price)  

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerset(self.model, using=self._db)

    def price_greater_than(self,price):
        return self.get_queryset().price_greater_than(price)
    



class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    sku = models.IntegerField(_("SKU"))
    brand = models.ForeignKey('Brand',verbose_name=_("Brand"),related_name='product_brand',on_delete=models.SET_NULL , null=True , blank=True)
    price = models.FloatField(_("Price"))
    desc = models.TextField(_("Desc"),max_length=10000)
    tags = TaggableManager(blank=True)
    flag = models.CharField(_("Flag"),max_length=10 ,choices=FLAG_TYPE)
    category = models.ForeignKey('Category',verbose_name=_("Category"),related_name='product_category',on_delete=models.SET_NULL , null=True , blank=True)
    slug = models.SlugField(null=True , blank=True)
    image = models.ImageField(upload_to='Products/')
    quantity = models.IntegerField(_("Quantity"),default=0)
    video_url = models.URLField(_("Video Url"),blank=True,null=True)
    
    objects = ProductManager()
    
    class Meta:
        # order_by = 'id' 
        verbose_name = 'product'
        verbose_name_plural = 'products'
    
    
    def save(self, *args, **kwargs):
       self.slug = slugify(self.name)    
       super(Product, self).save(*args, **kwargs) # Call the real save() method
    
    def __str__(self):
        return self.name
    
    # instance methods 
    def  get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'slug': self.slug})
    
    def get_avg_review(self):
        # rate_sum = 0
        
        avg =self.product_review.aggregate(myavg=Avg('rate'))
        # print(avg)
        # product_review = self.product_review.all()
        # for review in product_review:
        #     rate_sum += review.rate
        # print(rate_sum/len(product_review))
        return avg    
    
class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='product_image', on_delete=models.CASCADE)
    image = models.ImageField(_("image"),upload_to='product/')    
    def __str__(self):
        return str(self.product) 
 
    
    
class Brand(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    image = models.ImageField(_("image"),upload_to='brand/')   
    slug = models.SlugField(null=True , blank=True) 
    
    def __str__(self):
        return self.name    
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)    
        super(Brand, self).save(*args, **kwargs) # Call the real save() method
    
    
class Category(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    image = models.ImageField(upload_to='Category/',verbose_name=_("Image"))
    slug = models.SlugField(null=True , blank=True) 
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)    
        super(Category, self).save(*args, **kwargs)
    


class Review(models.Model):
    user = models.ForeignKey(User,verbose_name = _("User") ,related_name='review_author',on_delete=models.SET_NULL , null=True , blank=True)
    product = models.ForeignKey(Product, verbose_name=_("Product"),related_name='product_review', on_delete=models.CASCADE)
    review = models.TextField(_("Review"),max_length=500)
    rate = models.IntegerField(_("Rate"),validators=[MaxValueValidator(5),MinValueValidator(0)])
    created_at = models.DateTimeField(_("Created at"),default=timezone.now)
    
    def __str__(self):
        return f"{self.user.username} - {self.product.name}"
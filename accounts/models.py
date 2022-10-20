from django.db import models
from settings.models import Country , City
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from utils.generate_code import generaste_code
from products.models import Product
from django.utils.translation import gettext as _



class Profile(models.Model):
    user = models.OneToOneField(User,verbose_name=_("user"),related_name='Profile' ,on_delete=models.CASCADE)
    image = models.ImageField(_("Profile"),upload_to='profile/',null=True,blank=True)
    code = models.CharField(_("Code"),max_length=8 ,default=generaste_code)
    code_used = models.BooleanField(_("Code Used"),default=False)
    favourites = models.ManyToManyField(Product , related_name='favourite_products' ,verbose_name=_("Favourites"), null=True,blank=True)    
    def __str__(self):
        return self.user.username    
        
        
        
# create user -----> crate profile 
@receiver(post_save,sender=User)       
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user=instance)        
        
        
    
DATA_TYPE=(
    ('Home','Home'),
    ('Office','Office'),
    ('Bussines','Bussines'),
    ('Academy','Academy'),
    ('Others','Others'),
)    
    
class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User,related_name='UserPhone' ,verbose_name=_("User"),on_delete=models.CASCADE)
    phone_number = models.CharField(_("Phone Number"),max_length=15)
    type = models.CharField(_("Type"),max_length=10,choices=DATA_TYPE)

    def __str__(self):
        return f"{self.user.username} - {self.type}"    


class UserAddress(models.Model):
    user = models.ForeignKey(User,related_name='UserAddress' , verbose_name=_("User"),on_delete=models.CASCADE)
    type = models.CharField(_("Type"),max_length=10,choices=DATA_TYPE)
    country = models.ForeignKey(Country ,verbose_name=_("Country"), related_name='user_country' , on_delete=models.SET_NULL , null=True)
    city = models.ForeignKey(City , related_name='user_city' , verbose_name=_("City"),on_delete=models.SET_NULL , null=True)
    state = models.CharField(_("State"),max_length=50)
    region = models.CharField(_("Region"),max_length=50)
    street = models.CharField(_("Street"),max_length=50)
    notes = models.TextField(_("Notes"),max_length=300 , null=True , blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.type}"    
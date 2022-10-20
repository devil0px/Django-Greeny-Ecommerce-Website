from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Country(models.Model):
    name = models.CharField(_("Name"),max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Countries'


class City(models.Model):
    country = models.ForeignKey(Country,verbose_name=_("Country"), on_delete=models.CASCADE,related_name='country_city')
    name = models.CharField(_("Name"),max_length=50)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Cities'
        
        
        
        
class Company(models.Model):
    name = models.CharField(_("Name"),max_length=50)
    logo = models.ImageField(_("Logo"),upload_to='company/')
    about = models.CharField(_("About"),max_length=300)
    fb_link = models.URLField(_("fb_link"),null=True,blank=True)
    tw_link = models.URLField(_("tw_link"),null=True,blank=True)
    ins_link = models.URLField(_("ins_link"),null=True,blank=True)
    email = models.EmailField(_("email"),max_length=30)
    phone_number = models.CharField(_("phone number"),max_length=20)
    address = models.CharField(_("address"),max_length=100)
    
    def __str__(self):
        return self.name

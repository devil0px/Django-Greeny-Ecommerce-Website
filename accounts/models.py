

from django.db import models
from settings.models import Cauntry,City
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.




class Profile(models.Model):
    user = models.OneToOneField(User,related_name='profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/',null=True,blank=True)
    
    def __str__(self):
        return self.user.username
    
    
@receiver(post_save,sender=User)    
def create_profile(sender,instance,created,**kwargs):
    
    if created:
        Profile.objects.create(user=instance)


DATA_TYPE =(
    ('Home','Home' ),
    ('office','office' ),
    ('Bussines','Bussines' ),
    ('Acadeny','Acadenyw' ),
    ('Others','Others' ),
)
 
 
class UserPhoneNumber(models.Model):
    user = models.ForeignKey(User,related_name='UserPhone',on_delete=models.CASCADE)
    phone_number=models.CharField(max_length=11)
    type = models.CharField(max_length=10,choices=DATA_TYPE)
    
    def __str__(self):
        return f"{self.user.username} - {self.type}"






class UserAddress(models.Model):
    user = models.ForeignKey(User,related_name='UserAddress',on_delete=models.CASCADE)
    type = models.CharField(max_length=10,choices=DATA_TYPE)
    cauntry =models.ForeignKey(Cauntry,related_name='user_cauntry',on_delete=models.SET_NULL,null=True)
    city =models.ForeignKey(City,related_name='user_city',on_delete=models.SET_NULL,null=True)
    state =models.CharField(max_length=50)
    region =models.CharField(max_length=50)
    street =models.CharField(max_length=50)
    notes =models.TextField(max_length=500 ,null=True,blank=True)
    
    
    
    def __str__(self):
        return f"{self.user.username} - {self.type}"
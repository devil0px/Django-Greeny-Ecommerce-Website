
from django.db import models

# Create your models here.


class Cauntry (models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    
    class Meta:
       
        verbose_name_plural = 'Cauntries'
 
    
class City (models.Model):
    cauntry = models.name = models.ForeignKey(Cauntry, related_name='cauntry_city', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
    class Meta:
       
        verbose_name_plural = 'cities'
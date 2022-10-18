from django.db import models

# Create your models here.

class banner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=400)
    image = models.ImageField(upload_to='banner/')
    active = models.BooleanField(default=False)

    
    
    def __str__(self):
        return self.title
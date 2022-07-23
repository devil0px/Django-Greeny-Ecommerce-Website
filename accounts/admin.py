from django.contrib import admin

# Register your models here.
from .models import Profile , UserPhoneNumber ,UserAddress



admin.site.register(Profile)
admin.site.register(UserPhoneNumber)
admin.site.register(UserAddress)
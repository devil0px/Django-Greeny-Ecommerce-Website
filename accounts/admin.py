from atexit import register
from django.contrib import admin

# Register your models here.
from .models import Profile , UserAddress , UserPhoneNumber




admin.site.register(Profile)
admin.site.register(UserAddress)
admin.site.register(UserPhoneNumber)
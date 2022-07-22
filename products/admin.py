from django.contrib import admin

# Register your models here.
from .models import Product ,Brand ,Category,ProductImages,Reviews
from django_summernote.admin import SummernoteModelAdmin


class ProductImagesInline(admin.TabularInline):
    model = ProductImages
   

class ProductAdmin(SummernoteModelAdmin):
    inlines = [ProductImagesInline]
    summernote_fields = '__all__'

admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Reviews)
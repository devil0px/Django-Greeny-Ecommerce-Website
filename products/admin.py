from atexit import register
from django.contrib import admin
from .models import Product , Brand , Category , ProductImages , Review
from django_summernote.admin import SummernoteModelAdmin
from django.db.models.aggregates import Avg

class ProductImagesInline(admin.TabularInline):
    model = ProductImages


class ProductAdmin(SummernoteModelAdmin):
    list_per_page = 50
    inlines = [ProductImagesInline]
    summernote_fields = '__all__'
    list_display = ['name','review_count','rate_avg']
    # list_display = ['name']
    
    def review_count(self,obj):
        return obj.product_review.count()
    
    def rate_avg(self,obj):
        avg = obj.product_review.aggregate(Avg('rate'))
        return avg['rate__avg']



admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(ProductImages)
admin.site.register(Review)
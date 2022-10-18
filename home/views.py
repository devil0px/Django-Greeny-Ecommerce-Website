from django.shortcuts import render
from products.models import Category , Product , Brand , Review
from django.db.models import Count
from .models import banner

def home(request):
    categories = Category.objects.all().annotate(product_count=Count('product_category')) 
    featured_products = Product.objects.filter(flag='Feature')[:6]
    new_products = Product.objects.filter(flag='New')[:5]
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))  
    reviews = Review.objects.filter(rate=5)[:6]
    home_banner = banner.objects.filter(active=True)
    
    return render(request,'home/home.html',{
        'categories': categories,
        'featured_products':featured_products,
        'new_products':new_products , 
        'brands' :brands,
        'reviews': reviews,
        'home_banner':home_banner
    })
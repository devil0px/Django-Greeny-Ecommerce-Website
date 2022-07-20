from multiprocessing import get_context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from .models import Product ,ProductImages,Reviews,Category,Brand
from django.db.models import Count

# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 1

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct =self.get_object()        
        context["imags"] = ProductImages.objects.filter(product=myproduct)
        context ['reviews'] = Reviews.objects.filter(product=myproduct)
        return context

class CategoryLíst(ListView):
    model = Category
    paginate_by = 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] =Category.objects.all().annotate(product_count=Count('produc_Category'))
        return context
    
    
class BrandLíst(ListView):
    model = Brand
    paginate_by = 1
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['brands'] =Brand.objects.all().annotate(product_count=Count('produc_Prand'))
        return context    
    
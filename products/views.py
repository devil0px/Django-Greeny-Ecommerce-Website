from multiprocessing import get_context
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView,DetailView
from .models import Product ,ProductImages,Reviews

# Create your views here.

class ProductList(ListView):
    model = Product
    paginate_by = 1

class ProductDetail(DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        myproduct =self.get_object()
        print(myproduct)
        context = super().get_context_data(**kwargs)
        context["image"] = ProductImages.objects.filter(product=myproduct)
        context ['reviews'] = Reviews.objects.filter(product=myproduct)
        return context

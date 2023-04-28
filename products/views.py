from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView
from .models import Brand, Product , ProductImages , Review , Category
from django.db.models import Count
from django.db.models import Q , F , Func , Value
from django.db.models.aggregates import Count , Max , Min , Sum , Avg
from django.db.models.functions import Concat
# lazy query 
from django.db.models import CharField
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from .forms import ReviewForm
from django.urls import reverse
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
    
from django.http import JsonResponse
from django.template.loader import render_to_string  



# def product_list(request):
    
#     # querset = Product.objects.filter(name__endswith='fox' , price__gt=50)   # list 
#     # querset = Product.objects.filter(
#     #     Q(name__endswith='fox') &
#     #     ~Q(price__gt=50))
    
#     queryset = Product.objects.all()
#     # queryset.filter(name__endswith='fox').filter(price__gt=50)
    
    
#     # queryset = Product.objects.filter(id=F('category__id')).order_by('name')
#     # queryset = Product.objects.order_by('name')[0]
#     # queryset = Product.objects.latest('name')
#     # print(queryset)
#     # queryset = Product.objects.order_by('name')[20:30]
#     # queryset = Product.objects.values_list('id','name','category__name').distinct()
#     # queryset = Product.objects.only('id','name','category__name','price')
#     # queryset = Product.objects.defer('price')
#     # queryset = Product.objects.select_related('category').select_related('brand').all()  # foreignkey  , many : prefetch_related 

#     # queryset = Product.objects.aggregate(myavg=Avg('price'),mysum=Sum('price'))
#     # print(queryset)
    
#     # queryset = Product.objects.annotate(price_tax=F('price')*.8)
#     # queryset = Product.objects.annotate(
#     #     full_name = Concat('name','sku' , output_field=CharField())
#     # )
#     # queryset = Product.objects.price_greater_than(100)   # querset cache 
    
#     # list(queryset)
    
#     # list(queryset)
    
#     return render(request,'products/list.html',{'data':queryset})


# def product_list(request):
#     if cache.get(['queryset']) is None :
#         queryset = Product.objects.all()
#         cache.set('queryset',queryset)
    
#     print(cache.get(['queryset']))
#     return render(request,'products/list.html',{'data':cache.get(['queryset'])})


@cache_page(60 * 2)
def product_list(request):
    queryset = Product.objects.all()
    return render(request,'products/list.html',{'data':queryset})


def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def product_list_with_ajax(request):
    product = Product.objects.all()
    if is_ajax(request=request):
            print(' in ajax')
            min_price = request.GET['min_value']
            max_price = request.GET['max_value']
            queryset = Product.objects.filter(price__gt=min_price , price__lt=max_price)
            
            html = render_to_string('include/product_list_div.html',{'object_list':queryset , request:request})
            return JsonResponse({'result':html})
    return render(request,'products/product_list.html',{'object_list':product})

# @cache_page(60 * 15)
class ProductList(ListView):
    model = Product
    # paginate_by = 50
    
    # @method_decorator(cache_page(60 * 15))
    # def get_queryset(self):
    #     return super().get_queryset()
    
    def get_queryset(self):
        try:
            print(' in ajax')
            min_price = self.request.GET['min_value']
            max_price = self.request.GET['max_value']
            queryset = Product.objects.filter(price__gt=min_price , price__lt=max_price)
            
            html = render_to_string('include/product_list_div.html',{'object_list':queryset , self.request:self.request})
            return JsonResponse({'result':html})
        
        except:
            return super().get_queryset()
        

    
    

    
    
    
    
    
    
class ProductDetail(DetailView):
    model = Product
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        myproduct = self.get_object()
        context["images"] = ProductImages.objects.filter(product=myproduct) 
        context['reviews'] = Review.objects.filter(product=myproduct)
        context['related'] = Product.objects.filter(category=myproduct.category)[:10]
        return context
    
    def post(self, request, *args, **kwargs):
        myproduct = self.get_object()
        quantity = ''


    
@login_required  
def add_review(request,slug):
    print('in review')
    product = Product.objects.get(slug=slug)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        print(request.POST)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.user = request.user 
            myform.product = product 
            myform.save()
    
            # return redirect(reverse('products:product_detail', kwargs={'slug': slug}))
            reviews = Review.objects.filter(product=product)
            html = render_to_string('include/reviews.html',{'reviews':reviews , request:request})
            return JsonResponse({'result':html})
    
    
class CategoryList(ListView):
    model = Category
    paginate_by = 20
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     context['categories'] = Category.objects.all().annotate(product_count=Count('product_category'))   
    #     return context
    
    def get_queryset(self):
        queryset = super(CategoryList, self).get_queryset()
        queryset = Category.objects.all().annotate(product_count=Count('product_category'))   
        return queryset

    
    
class CategoryDetail(DetailView):
    pass   
    
    
class BrandList(ListView):
    model = Brand
    paginate_by = 20


    def get_queryset(self):
        queryset = super(BrandList, self).get_queryset()
        queryset = Brand.objects.all().annotate(product_count=Count('product_brand'))
        return queryset

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs) 
    #     context['brands'] = Brand.objects.all().annotate(product_count=Count('product_brand'))   
    #     return context
    
    # object_list , brand_list , brands
    
    
class BrandDetail(ListView):
    model = Product
    template_name='products/brand_detail.html'
    
    
    def get_queryset(self):
        brand_slug = self.kwargs['slug']
        queryset = Product.objects.filter(brand__slug=brand_slug)
        return queryset
    
    
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     brand = self.get_object()
    #     context["brand_products"] = Product.objects.filter(brand=brand)
    #     return context
    
    
    
    
    
    
# @login_required    
# def add_review(request):
#     pass    
    

@login_required     
def add_to_favourites(request):
    product = Product.objects.get(id=request.POST['productid'])
    profile = Profile.objects.get(user=request.user)
    
    if product in profile.favourites.all():
        profile.favourites.remove(product)
    else:
        profile.favourites.add(product)
from django.shortcuts import render , redirect
from .forms import SignupForm , UserActivateForm
from .models import Profile , UserAddress , UserPhoneNumber
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from .task import print_welcome
from django.contrib.auth.decorators import user_passes_test


from products import models as product_models 
from orders import models as orders_models 
from django.contrib.auth.models import User

'''
    - data 
    - send activation code [email - phone_number]

'''



def signup(request):
    '''
        form ---> data[submit] -------> 
        create account[not active] ------> 
        [send activation code] [redirect:form[activation code]] -->
        [active] - redirect:profile
    
    '''
    
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            
            
            myform = form.save(commit=False)
            myform.active = False
            myform.save()
            profile = Profile.objects.get(user__username=username)
            print(profile)
            print(profile.code)
            # code = 12345
            send_mail(
                subject='Activate your account',
                message=f'use this code {profile.code} to activate your account',
                from_email='pythondeveloper6@gmail.com',
                recipient_list=[email],
                fail_silently=False,
            )
            return redirect(f'/accounts/{username}/activate')
        
    else:
        form = SignupForm()
        
    return render(request,'registration/signup.html', {'form':form})


def user_activate(request,username):
    profile = Profile.objects.get(user__username=username)
    if request.method == 'POST':
        form = UserActivateForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data['code']
            if profile.code == code : 
                profile.code_used = True
                profile.save()
                return redirect('/accounts/login')
        
    else:
        form = UserActivateForm()
    return render(request,'registration/activate.html',{'form':form})
    



@login_required
def profile(request):
    profile =  Profile.objects.get(user=request.user)
    phone_number = UserPhoneNumber.objects.filter(user=request.user)
    user_address = UserAddress.objects.filter(user=request.user)
    return render(request,'registration/profile.html',{'profile':profile,'phone_number':phone_number,'user_address':user_address})


def wishlist(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'registration/wishlist.html',{'profile':profile})


import time



def test_celery(request):
    print_welcome.delay(10)
    # time.sleep(10)
    # print('welcome')
    
    return render(request,'test.html',{})


@user_passes_test(lambda u: u.is_superuser)
def dashboard(request):
    user = User.objects.all().count()
    products = product_models.Product.objects.all().count()
    review = product_models.Review.objects.all().count()
    brand = product_models.Brand.objects.all().count()
    category = product_models.Category.objects.all().count()
    orders = orders_models.Order.objects.all().count()
    
    inprogress_orders = orders_models.CartOrder.objects.filter(order_status='Inprogress').count()
    recieved_orders = orders_models.Order.objects.filter(order_status='Recieved').count()
    processed_orders = orders_models.Order.objects.filter(order_status='Processed').count()
    shipped_orders = orders_models.Order.objects.filter(order_status='Shipped').count()
    delivered_orders = orders_models.Order.objects.filter(order_status='Delivered').count()
    
    
    
    return render(request,'accounts/dashboard.html',{
        'inprogress_orders' : inprogress_orders , 
        'recieved_orders' :recieved_orders ,
        'processed_orders' : processed_orders , 
        'shipped_orders' : shipped_orders , 
        'delivered_orders' : delivered_orders , 
        
        'user' : user , 
        'products' : products , 
        'review' : review , 
        'brand' : brand , 
        'category' : category , 
        'orders' : orders  
    })
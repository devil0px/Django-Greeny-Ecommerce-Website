from django.shortcuts import render , redirect
from .forms import SignupForm , UserActivateForm
from .models import Profile , UserAddress , UserPhoneNumber
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
# Create your views here.

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
from django.urls import path 
from .views import signup , user_activate , profile , wishlist,test_celery

app_name='accounts'




urlpatterns = [
    path('test',test_celery),
    path('signup/' , signup , name='signup'),
    path('profile/' , profile , name='profile'),
    path('profile/wishlist' , wishlist , name='wishlist'),
    path('<str:username>/activate' , user_activate , name='user_activate'),

]

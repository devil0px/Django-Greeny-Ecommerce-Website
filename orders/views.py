from django.shortcuts import render
from .models import Order , OrderDetail , CartOrder , CartOrderDetail , Coupon
from django.contrib.auth.decorators import login_required
from products.models import Product
from django.shortcuts import get_object_or_404
from django.utils.timezone import datetime 
from django.http import JsonResponse
from django.template.loader import render_to_string    


@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)

    return render(request,'orders/order_list.html',{'orders':orders})




def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['productid']
        quantity= request.POST['quanitity']
        
        product = Product.objects.get(id=product_id)
        cart = CartOrder.objects.get(user=request.user,order_status='Inprogress')
        cart_detail , created =  CartOrderDetail.objects.get_or_create(
            order = cart ,
            product = product
        )
        cart_detail.quantity = int(quantity)
        cart_detail.price = product.price
        cart_detail.total = int(quantity) * product.price
        cart_detail.save()
        
        cart_details = CartOrderDetail.objects.filter(order=cart.id)
        cart = CartOrder.objects.get(user=request.user,order_status='Inprogress')
        html = render_to_string('include/cart_side.html',{'cart':cart , 'crt_detail':cart_details, request:request})
        cart_total = round(cart.get_total(),2)
        return JsonResponse({'result':html , 'total':cart_total})
            
        
        
        
@login_required
def checkout_page(request):
    cart = CartOrder.objects.get(user=request.user,order_status='Inprogress')
    cart_detail =  CartOrderDetail.objects.filter(
        order = cart ,
    )
    
    # delivery , coupon 
    delivery_cost = 50
    today_date = datetime.today().date()
    cart_total = cart.get_total()
    if request.method == 'POST':
        print(request.POST)
        code = request.POST['code']
        print(f" code = {code}")
        coupon_code = get_object_or_404(Coupon,code=code)
        if coupon_code and coupon_code.quantity > 0: 
            print('in if ')
            if today_date >= coupon_code.from_date and today_date <= coupon_code.to_date:
                code_value = cart.get_total() /100 * coupon_code.value
                total = cart.get_total() - code_value
                total = total+ delivery_cost
                html = render_to_string('include/total.html',{'cart_total':cart_total,'delivery_cost':delivery_cost ,'code_value':code_value,'total':total, request:request})
                return JsonResponse({'result':html})
            else:
                # in valid
                pass
    
    print('outside if')
    total = cart_total + delivery_cost
    return render(request,'orders/checkout.html',{'cart':cart ,'cart_total':cart_total, 'cart_Detail':cart_detail,'total':total,'delivery_cost':delivery_cost})
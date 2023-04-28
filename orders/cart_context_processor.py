from .models import CartOrder , CartOrderDetail


def get_or_create_cart(request):
    if request.user.is_authenticated:
        cart , created = CartOrder.objects.get_or_create(user=request.user,order_status='Inprogress')
        cart_detail = CartOrderDetail.objects.filter(order=cart.id)
        return {'cart':cart , 'crt_detail':cart_detail}
    
    else:
        return {}
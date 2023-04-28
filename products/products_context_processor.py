from .models import Brand , Category





def get_brands(request):
    brands = Brand.objects.all()
    if len(brands) > 0:
        return {'c_brands':brands}
    else:
        return {}



def get_favourites(request):
    pass
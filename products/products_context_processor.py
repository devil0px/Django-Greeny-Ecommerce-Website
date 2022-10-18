from .models import Brand , Category





def get_brands(request):
    brands = Brand.objects.all()
    return {'c_brands':brands}



def get_favourites(request):
    pass
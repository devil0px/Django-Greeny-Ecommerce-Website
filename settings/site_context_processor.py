from .models import Company



def get_site_info(request):
    site_info = Company.objects.last()
    return {'site_info' : site_info}
from .models import Profile


def get_user(request):
    profile = Profile.objects.get(user=request.user)
    return {'profile':profile}
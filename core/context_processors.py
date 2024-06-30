from .models import SiteSettings, AboutUs

def site_settings(request):
    settings = SiteSettings.objects.first()
    return {'site_settings': settings}

def site_about(request):
    site_about = AboutUs.objects.first()
    return {'site_about': site_about}
from django.shortcuts import render, get_object_or_404, redirect
from .models import *

from django.core.mail import send_mail
from django.conf import settings
import smtplib
from django.http import HttpResponse

# Create your views here.
def index(request):
    about = AboutUs.objects.first()
    services = PracticeArea.objects.all()
    teams = TeamMember.objects.all()
    clients = Client.objects.all()
    sliders = Slider.objects.all()
    blogs = Blog.objects.all()[:3]

    context = {
        'about': about,
        'services': services,
        'teams': teams,
        'clients': clients,
        'sliders': sliders,
        'blogs':blogs
    }
    return render(request, 'index.html', context)

def about(request):
    about = AboutUs.objects.first()
    context = {
        'about' : about
    }
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')

        if not all([message, name, email, subject]):
            return redirect('core:contact')

        contact = ContactUs(message=message, name=name, email=email, subject=subject)
        contact.save()

        try:
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ['info@Prominentlawfirm.com'],
                fail_silently=False,
            )
        except Exception as e:
            print(e)
            return HttpResponse(f'SMTP error occurred: {e}')

        return redirect('core:contact')

    contact = SiteSettings.objects.first()
    context = {
        'contact' : contact
    }
    return render(request, 'contact.html', context)

def service(request):
    services = PracticeArea.objects.all()
    context = {
        'services' : services
    }
    return render(request, 'service.html', context)

def team(request):
    teams = TeamMember.objects.all()
    context = {
        'teams' : teams
    }
    return render(request, 'team.html', context)

def video(request):
    videos = Video.objects.all()
    return render(request, 'video.html', {'videos': videos})

def blog(request):
    blogs = Blog.objects.all().order_by('-id')
    context = {
        'blogs' : blogs
    }
    return render(request, 'blog.html', context)

def single_blog(request, blog_id):
    try:
        blog = get_object_or_404(Blog, pk=blog_id)
    except Blog.DoesNotExist:
        return redirect('core:blog')
    except Exception as e:
        return redirect('core:blog')
    context = {
        'blog' : blog
    }
    return render(request, 'single_blog.html', context)
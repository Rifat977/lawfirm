from django.urls import path
from core import views

app_name = "core"

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('practice-areas/', views.service, name="service"),
    path('attorneys/', views.team, name="team"),
    path('blog/', views.blog, name="blog"),
    path('videos/', views.video, name="video"),
    path('single-blog/<int:blog_id>/', views.single_blog, name="single_blog"),
]

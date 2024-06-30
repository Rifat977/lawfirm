from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from taggit.managers import TaggableManager

from django.utils.html import mark_safe
from django.utils.safestring import mark_safe

from urllib.parse import urlparse, parse_qs

class Slider(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='slider/', help_text='Image dimensions should be 1500px (width) by 800px (height).')

    def save(self, *args, **kwargs):
        if self.pk:
            original = Slider.objects.get(pk=self.pk)
            if original.image != self.image:
                original.image.delete(save=False)
        super().save(*args, **kwargs)


class AboutUs(models.Model):
    image1 = models.ImageField(upload_to='about/')
    image2 = models.ImageField(upload_to='about/')
    title = models.CharField(max_length=200)
    text = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk:
            original = AboutUs.objects.get(pk=self.pk)
            if original.image1 != self.image1:
                original.image1.delete(save=False)
            if original.image2 != self.image2:
                original.image2.delete(save=False)
        super().save(*args, **kwargs)


class PracticeArea(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='practice_areas/')
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk:
            original = PracticeArea.objects.get(pk=self.pk)
            if original.image != self.image:
                original.image.delete(save=False)
        super().save(*args, **kwargs)

class Service(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='services/')
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk:
            original = Service.objects.get(pk=self.pk)
            if original.image != self.image:
                original.image.delete(save=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()

    def save(self, *args, **kwargs):
        if self.pk:
            original = TeamMember.objects.get(pk=self.pk)
            if original.image != self.image:
                original.image.delete(save=False)
        super().save(*args, **kwargs)


class Client(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='clients/')

    def save(self, *args, **kwargs):
        if self.pk:
            original = Client.objects.get(pk=self.pk)
            if original.image != self.image:
                original.image.delete(save=False)
        super().save(*args, **kwargs)


class Blog(models.Model):
    image = models.ImageField(upload_to='blog/')
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    content = HTMLField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.pk:
            original = Blog.objects.get(pk=self.pk)
            if original.image != self.image:
                original.image.delete(save=False)
        super().save(*args, **kwargs)

class ContactUs(models.Model):
    message = models.TextField()
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)

class SiteSettings(models.Model):
    company_name = models.CharField(max_length=200)
    email = models.EmailField()
    site = models.URLField()
    phone_number_1 = models.CharField(max_length=20)
    phone_number_2 = models.CharField(max_length=20, blank=True, null=True)
    evening_chamber_location = models.CharField(max_length=200)
    court_chamber_location = models.CharField(max_length=200)
    logo = models.FileField(upload_to='logos/', help_text='Image dimensions should be 250px (width) by 75px (height).')
    practice_areas = models.TextField(null=True, blank=True)
    linkedin_url = models.URLField(blank=True, null=True)
    facebook_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.pk:
            original = SiteSettings.objects.get(pk=self.pk)
            if original.logo != self.logo:
                original.logo.delete(save=False)
        else:
            SiteSettings.objects.exclude(pk=self.pk).delete()

        super().save(*args, **kwargs)

    def clean(self):
        if SiteSettings.objects.exclude(pk=self.pk).exists():
            raise ValidationError("There can only be one instance of SiteSettings.")


class Video(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField()

    def get_video_id(self):

        url_data = urlparse(self.url)
        if url_data.hostname == 'youtu.be':
            return url_data.path[1:]
        if url_data.hostname in ('www.youtube.com', 'youtube.com'):
            if url_data.path == '/watch':
                return parse_qs(url_data.query)['v'][0]
            if url_data.path[:7] == '/embed/':
                return url_data.path.split('/')[2]
            if url_data.path[:3] == '/v/':
                return url_data.path.split('/')[2]
        return None

    def __str__(self):
        return self.title
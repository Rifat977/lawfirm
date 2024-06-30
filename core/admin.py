from django.contrib import admin
from .models import *

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'text')

@admin.register(PracticeArea)
class PracticeAreaAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'description')

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'title')
    search_fields = ('name', 'title', 'description')

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_date', 'category')
    search_fields = ('title', 'content', 'author__username', 'category')
    list_filter = ('publication_date', 'category', 'tags')
    prepopulated_fields = {"title": ("title",)}

@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject', 'message')

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'email', 'phone_number_1', 'phone_number_2')
    search_fields = ('company_name', 'email', 'phone_number_1', 'phone_number_2', 'evening_chamber_location', 'court_chamber_location')

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')

# Optionally, register models without custom admin configurations
# admin.site.register(AboutUs, AboutUsAdmin)
# admin.site.register(PracticeArea, PracticeAreaAdmin)
# admin.site.register(TeamMember, TeamMemberAdmin)
# admin.site.register(Client, ClientAdmin)
# admin.site.register(Blog, BlogAdmin)
# admin.site.register(ContactUs, ContactUsAdmin)
# admin.site.register(SiteSettings, SiteSettingsAdmin)

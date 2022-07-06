from django.contrib import admin
from .models import Profile,BlogPost

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user','bio','url']


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['user','title','content','date_updated','date_created']

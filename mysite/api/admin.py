from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Removed 'author'
    fields = ('title', 'content')  # Removed 'author'

admin.site.register(BlogPost, BlogPostAdmin)
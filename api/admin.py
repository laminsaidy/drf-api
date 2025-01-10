from django.contrib import admin
from .models import BlogPost

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')  # Display 'title' and 'published_date' columns in the list view
    fields = ('title', 'content')  # Only allow 'title' and 'content' fields to be editable in the form

admin.site.register(BlogPost, BlogPostAdmin)
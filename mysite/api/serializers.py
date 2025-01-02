from rest_framework import serializers
from .models import BlogPost

class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published_date', 'author', 'id']  # Include author

    # Optionally, you can use a custom method to get the author's name
    def get_author(self, obj):
        return obj.author.username  # Return the author's username instead of the User object
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny  # Allow access to anyone
from .models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes = [AllowAny]  # Allow everyone to access this view (no auth required)

    def perform_create(self, serializer):
        # If you still want to keep the 'author' as an authenticated user, 
        # you can modify this to allow anonymous user, or set a default value
        serializer.save(author=None)  # Assign 'author' as None if no user is authenticated

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
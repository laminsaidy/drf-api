from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost
from .serializers import BlogPostSerializer

from rest_framework.views import APIView  # Add this import

class UpdateBlogPosts(APIView):
    def put(self, request, *args, **kwargs):
        new_data = request.data
        BlogPost.objects.all().update(**new_data)
        return Response({"message": "Blog posts updated successfully"}, status=status.HTTP_200_OK)



class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class BlogPostRetrieveUpdateDestory(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"
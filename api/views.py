from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import BlogPost, Vote, Category
from .serializers import BlogPostSerializer, VoteSerializer, CategorySerializer
from django.db.models import Q

class VoteListView(APIView):
    def get(self, request, post_id, *args, **kwargs):
        # Get all votes for the given post
        votes = Vote.objects.filter(post_id=post_id)
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def vote_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    
    # If no existing vote, create a new one
    vote = Vote.objects.create(post=post, vote_type=request.data['vote_type'])
    return Response(VoteSerializer(vote).data, status=status.HTTP_201_CREATED)

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

class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

# Search for blog posts by title or content
class BlogPostSearchView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return BlogPost.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )

# Filter blog posts by category
class BlogPostCategoryFilterView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        category_id = self.request.query_params.get('category_id', None)
        if category_id:
            return BlogPost.objects.filter(category_id=category_id)
        return BlogPost.objects.all()
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import BlogPost, Vote, Category
from .serializers import BlogPostSerializer, VoteSerializer, CategorySerializer
from django.db.models import Q

# Get all votes for a given post
class VoteListView(APIView):
    def get(self, request, post_id, *args, **kwargs):
        votes = Vote.objects.filter(post_id=post_id)
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# Create or check vote for a post
@api_view(['POST'])
def vote_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    
    # Check if the user has already voted
    user = request.user  # Assuming you have user authentication set up
    existing_vote = Vote.objects.filter(post=post, user=user).first()
    
    if existing_vote:
        return Response({"detail": "You have already voted on this post."}, status=status.HTTP_400_BAD_REQUEST)

    # If no existing vote, create a new one
    vote = Vote.objects.create(post=post, vote_type=request.data['vote_type'], user=user)
    return Response(VoteSerializer(vote).data, status=status.HTTP_201_CREATED)

# Update blog posts (modifies all posts)
class UpdateBlogPosts(APIView):
    def put(self, request, *args, **kwargs):
        new_data = request.data
        BlogPost.objects.all().update(**new_data)
        return Response({"message": "Blog posts updated successfully"}, status=status.HTTP_200_OK)

# Update a specific blog post
class UpdateBlogPost(APIView):
    def put(self, request, post_id, *args, **kwargs):
        try:
            post = BlogPost.objects.get(id=post_id)
            for key, value in request.data.items():
                setattr(post, key, value)
            post.save()
            return Response({"message": "Blog post updated successfully"}, status=status.HTTP_200_OK)
        except BlogPost.DoesNotExist:
            return Response({"detail": "Blog post not found."}, status=status.HTTP_404_NOT_FOUND)

# List or create blog posts
class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()  
        return Response(status=status.HTTP_204_NO_CONTENT)

# Retrieve, update, or delete a single blog post
class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = "pk"

# Search for blog posts by title or content
class BlogPostSearchView(generics.ListAPIView):
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        if not query:
            return BlogPost.objects.none()  # Return no results if query is empty
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
        return BlogPost.objects.all()  # Return all blog posts by default
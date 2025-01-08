from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from .models import BlogPost, Vote
from .serializers import BlogPostSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .serializers import VoteSerializer

class VoteListView(APIView):
    def get(self, request, post_id, *args, **kwargs):
        # Get all votes for the given post
        votes = Vote.objects.filter(post_id=post_id)
        serializer = VoteSerializer(votes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def vote_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)

    # Check if the user has already voted on this post
    existing_vote = Vote.objects.filter(user=request.user, post=post).first()
    if existing_vote:
        existing_vote.vote_type = request.data['vote_type']
        existing_vote.save()
        return Response(VoteSerializer(existing_vote).data)

    # If no existing vote, create a new one
    vote = Vote.objects.create(user=request.user, post=post, vote_type=request.data['vote_type'])
    return Response(VoteSerializer(vote).data, status=status.HTTP_201_CREATED)


from rest_framework.views import APIView  

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
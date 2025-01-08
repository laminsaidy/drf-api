from rest_framework import serializers
from .models import BlogPost, Vote, Comment

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'post', 'vote_type', 'created_at']

class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()  # Display username instead of user ID
    post = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all())  # Link to BlogPost

    class Meta:
        model = Comment
        fields = ['id', 'user', 'post', 'content', 'created_at', 'updated_at']

class BlogPostSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)  # Fetch comments for each blog post

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published_date', 'author', 'id', 'vote_count', 'comments']

    def get_vote_count(self, obj):
        return obj.votes.count()  
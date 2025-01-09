from rest_framework import serializers
from .models import BlogPost, Vote, Comment, Category

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

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']  # Include the category ID and name

class BlogPostSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()
    comments = CommentSerializer(many=True, read_only=True)  # Fetch comments for each blog post
    category = CategorySerializer()  # Include category information in the BlogPostSerializer

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published_date', 'author', 'id', 'vote_count', 'comments', 'category']

    def get_vote_count(self, obj):
        return obj.votes.count()
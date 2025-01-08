from rest_framework import serializers
from .models import BlogPost
from .models import Vote

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id', 'user', 'post', 'vote_type', 'created_at']

class BlogPostSerializer(serializers.ModelSerializer):
    vote_count = serializers.SerializerMethodField()

    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'published_date', 'author', 'id', 'vote_count']

    def get_vote_count(self, obj):
        return obj.votes.count()  # Returns the count of votes for this post
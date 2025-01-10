from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Signal to ensure a default category is created after migrations
@receiver(post_migrate)
def create_default_category(sender, **kwargs):
    if sender.name == "api":  # Replace "api" with your app name
        Category.objects.get_or_create(id=1, defaults={"name": "Default"})

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.title

class Vote(models.Model):
    UPVOTE = 'up'
    DOWNVOTE = 'down'
    VOTE_CHOICES = [
        (UPVOTE, 'Upvote'),
        (DOWNVOTE, 'Downvote'),
    ]

    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='votes')
    vote_type = models.CharField(max_length=4, choices=VOTE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f" {self.vote_type}d {self.post.title}"

class Comment(models.Model):
    post = models.ForeignKey(BlogPost, on_delete=models.CASCADE, related_name='comments')  
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    content = models.TextField() 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"

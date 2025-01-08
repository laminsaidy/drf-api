from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost_list_create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestory.as_view(), name="update"),
    path('blogposts/<int:post_id>/vote/', views.vote_post, name='vote_post'),
    path('blogposts/<int:post_id>/votes/', views.VoteListView.as_view(), name='vote_list'),  # Corrected the path
]
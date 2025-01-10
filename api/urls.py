from django.urls import path
from . import views

urlpatterns = [
    # Redirect from the root URL to /blogposts/
    path('', lambda request: redirect('/blogposts/')),

    # Existing URL paths
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost_list_create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name="update"),
    path('blogposts/<int:post_id>/vote/', views.vote_post, name='vote_post'),
    path('blogposts/<int:post_id>/votes/', views.VoteListView.as_view(), name='vote_list'),
    path('blogposts/search/', views.BlogPostSearchView.as_view(), name='blogpost_search'),
    path('blogposts/category/', views.BlogPostCategoryFilterView.as_view(), name='blogpost_category_filter'),
]
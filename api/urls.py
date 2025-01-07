from django.urls import path
from . import views

urlpatterns = [
    path('blogposts/', views.BlogPostListCreate.as_view(), name='blogpost_list_create'),
    path(
        "blogposts/<int:pk>/",
        views.BlogPostRetrieveUpdateDestory.as_view(),
        name="update",
    ),
]
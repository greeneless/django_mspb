from django.contrib import admin
# Do we still need this?
from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('forum/', views.forum, name='forum-forum'),
    path('forum/user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('forum/post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('forum/post/new/', PostCreateView.as_view(), name='post-create'),
    path('forum/post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('forum/post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
]

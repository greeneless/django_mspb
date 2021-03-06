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
    path('', views.home, name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('rmm-suite/administration', views.administration, name='blog-rmmsuite-administration'),
    path('rmm-suite/how-do-i', views.how_do_i, name='blog-rmmsuite-how-do-i'),
    path('about/staff', views.staff, name='blog-staff'),
    path('contact/', views.contact, name='blog-contact'),
    path('rmm-suite/', views.rmm_suite, name='blog-rmmsuite'),
    path('rmm-suite/documentation', views.documentation, name='blog-rmmsuite-documentation'),
    path('rmm-suite/help', views.support_request, name='blog-rmmsuite-help'),
    path('blog/', PostListView.as_view(), name='blog-blog'),
]

# Class based URL views look for :
# # <app> + / + <model> + _ + <viewtype>
# # blog/post_list


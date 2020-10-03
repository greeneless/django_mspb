from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import ForumPost
from .forms import *


class PostListView(ListView):
    model = ForumPost
    template_name = 'blog/blog.html'  # <app> + / + <model> + _ + <viewtype>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = ForumPost
    template_name = 'blog/user_posts.html'  # <app> + / + <model> + _ + <viewtype>
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ForumPost.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = ForumPost


class PostCreateView(LoginRequiredMixin, CreateView):
    model = ForumPost
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ForumPost
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ForumPost
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

#
# def forum(request):
#     context = {'posts': ForumPost.objects.all()}
#     return render(request, 'forum/forum.html', context)


def forum(request):
    forums = Forum.objects.all()
    count = forums.count()
    discussions = [i.discussion_set.all() for i in forums]

    context = {
        'forums': forums,
        'count': count,
        'discussions': discussions
    }
    return render(request, 'forum.html', context)


def add_in_forum(request):
    form = CreateInForum()
    if request.method == 'POST':
        form = CreateInForum(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'add_in_forum.html', context)


def add_in_discussion(request):
    form = CreateInDiscussion()
    if request.method == 'POST':
        form = CreateInDiscussion(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'add_in_discussion.html', context)

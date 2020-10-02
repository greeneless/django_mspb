from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post


def home(request):
    return render(request, 'blog/home.html', {'title': 'Blog'})


class PostListView(ListView):
    model = Post
    template_name = 'blog/blog.html'  # <app> + / + <model> + _ + <viewtype>
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'  # <app> + / + <model> + _ + <viewtype>
    context_object_name = 'posts'
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = [
        'title',
        'content',
    ]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
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
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


def administration(request):
    return render(request, 'blog/rmm-suite/administration.html', {'title': 'Admin Tools'})


def contact(request):
    return render(request, 'blog/contact.html', {'title': 'Contact Us'})


def documentation(request):
    return render(request, 'blog/rmm-suite/documentation.html', {'title': 'Technician Manuals'})


def how_do_i(request):
    return render(request, 'blog/rmm-suite/how-do-i.html', {'title': 'How Do I...'})


def staff(request):
    return render(request, 'blog/about/staff.html', {'title': 'Our Team'})


def blog(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/blog.html', context)


def rmm_suite(request):
    return render(request, 'blog/rmm-suite.html', {'title': 'Tech Specs'})

from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from .models import CallForAction


def index(request):
    """Render the department homepage with recent blog posts."""
    recent_posts = Blog.objects.filter(published=True)[:3]
    all_posts = Blog.objects.filter(published=True)
    call_for_blogs = CallForAction.objects.all()
    return render(request, 'index.html', {'recent_posts': recent_posts, 'all_posts': all_posts, 'call_for_blogs': call_for_blogs})


# def blog_list(request):
#     """List all published blog posts."""
#     posts = Blog.objects.filter(published=True)
#     return render(request, 'blog_list.html', {'posts': posts})


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, "blog_detail.html", {"post": post})
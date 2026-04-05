from django.shortcuts import get_object_or_404, render
from blog.models import Blog

def blogPage(request):
    """Render the department homepage with recent blog posts."""
    recent_posts = Blog.objects.filter(published=True)[:3]
    all_posts = Blog.objects.filter(published=True)
    return render(request, 'blog_page.html', {'recent_posts': recent_posts, 'posts': recent_posts})

def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug)
    return render(request, "blog_detail.html", {"post": post})

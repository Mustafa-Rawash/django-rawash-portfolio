from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Blog

def blog_home(request):
    all_blogs = Blog.objects.all()
    return render(request, 'blog/blog_home.html', {'all_blogs':all_blogs})

def blog_post(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/blog_post.html', {'blog':blog})
from django.shortcuts import render
from blog.models import Blog
# Create your views here.


def blogs(request):
    context = {
        "blogs": Blog.objects.all()
    }
    return render(request, 'blog.html', context)


def blog_detail(request, pk):
    context = {
        "blog": Blog.objects.get(pk=pk)
    }
    return render(request, 'blog_detail.html', context)

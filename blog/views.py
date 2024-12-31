from django.shortcuts import render
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render 
from .models import Blog

# Create your views here.

def all_blogs_view(request:HttpRequest):
    blogs = Blog.objects.all()
    context = {
        'blogs':blogs
    }
    return render(request,'blog/all_blogs.html',context=context)


def blog_view(request:HttpRequest,slug:str):
    blog = get_object_or_404(Blog,slug=slug)
    context = {
        'blog':blog
    }
    return render(request,'blog/blog_page.html',context=context)



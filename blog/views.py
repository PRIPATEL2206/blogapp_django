from django.shortcuts import render
from django.http.request import HttpRequest
from django.shortcuts import get_object_or_404
from django.shortcuts import render 
from .models import Blog
from django.db.models import Q

from django.core.paginator import Paginator


# Create your views here.

def all_blogs_view(request:HttpRequest):
    blogs=[]
    page_number = request.GET.get('page',1)
    search=request.GET.get('search',"")
    if request.GET:
        blogs=Blog.objects.filter(
            Q(title__icontains=search) |
            Q(heading__icontains=search) |
            Q(tags__title__icontains=search) |
            Q(descreption__icontains=search)
        )
    else:
        blogs = Blog.objects.all()

    paginatore= Paginator(blogs,6)
    try:
        page = paginatore.get_page(page_number)
    except:
        page = paginatore.get_page(1)
        
    other_pages=range(max(1,page.number-2),min(paginatore.num_pages,page.number+2)+1)
    
    context = {
         'page':page,
        "total":paginatore.count,
        "total_pages":paginatore.num_pages,
        'other_pages':other_pages,
        "search":search
    }
    return render(request,'blog/all_blogs.html',context=context)


def blog_view(request:HttpRequest,slug:str):
    blog = get_object_or_404(Blog,slug=slug)
    context = {
        'blog':blog
    }
    return render(request,'blog/blog_page.html',context=context)
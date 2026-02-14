from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .models import Blog,category

# Create your views here.

def posts_by_category(request,category_id):

    posts=Blog.objects.filter(status="Published",category=category_id)
    # try:
    #     Category = category.objects.get(pk=category_id)
    # except:
    #     return redirect('home')
    Category = get_object_or_404(category,pk=category_id)
    context ={
        "posts": posts,
        "category":Category,    
    }
    return render(request,'posts_by_category.html',context) 

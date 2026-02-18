from   django.http import HttpResponse
from django.shortcuts import render 
from blogs.models import Blog, category
from Assignments.models import About

def home(request):
    # return HttpResponse("<h1> Home Page <h1>")
    featured_posts =Blog.objects.filter(is_featured=True,status="Published").order_by("updated_at")
    posts =Blog.objects.filter(is_featured=False,status="Published")

    # for about us
    try:
        about=About.objects.get()
    except:
        about=None

    context ={
        'featured_posts':featured_posts,
        'posts':posts,
        'about':about,
    }
    return render(request,'home.html',context)
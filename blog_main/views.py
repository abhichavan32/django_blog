from   django.http import HttpResponse
from django.shortcuts import render 
from blogs.models import Blog, category

def home(request):
    # return HttpResponse("<h1> Home Page <h1>")
    categories = category.objects.all()
    featured_posts =Blog.objects.filter(is_featured=True,status="Published").order_by("updated_at")
    posts =Blog.objects.filter(is_featured=False,status="Published")

    context ={ 
        'categories':categories,
        'featured_posts':featured_posts,
        'posts':posts,
    }
    return render(request,'home.html',context)
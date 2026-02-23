from django.shortcuts import get_object_or_404, redirect, render

from blogs.models import Blog, category
from django.contrib.auth.decorators import login_required

from dashboards.forms import BlogPostForm, CategoryForm
from django.template.defaultfilters import slugify

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    category_count = category.objects.all().count()
    blogs_count = Blog.objects.all().count()
    context = {
        "category_count":category_count,
        "blogs_count":blogs_count,
    }
    return render(request,'dashboard/dashboard.html',context)


def categories(request):
    return render(request,'dashboard/categories.html')

def add_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')

    form=CategoryForm()
    context={
        "form":form,
    }
    return render(request,'dashboard/add_category.html',context)

def edit_category(request,pk):
    cat= get_object_or_404(category,pk=pk)

    if request.method =="POST":
        form =CategoryForm(request.POST,instance=cat)
        if form.is_valid():
            form.save()
            return redirect('categories')
    form = CategoryForm(instance=cat)
    context ={
        "form":form,
        "cat":cat,
    }
    return render(request,"dashboard/edit_category.html",context)

def delete_category(request,pk):
    cat = get_object_or_404(category,pk=pk)
    cat.delete()
    return redirect('categories')


def posts(request):
    posts = Blog.objects.all()
    context = {
        "posts":posts
    }
    return render(request,"dashboard/posts.html",context)

def add_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST,request.FILES)
        if form.is_valid():
            post= form.save(commit=False)
            post.author = request.user
            post.save()
            title=form.cleaned_data["title"]
            post.slug = slugify(title) + "-" + (post.id)
            post.save()
            return redirect("posts")
    form = BlogPostForm()
    context ={
        "form":form
    }
    return render(request,"dashboard/add_post.html",context)

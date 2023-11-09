from django.shortcuts import render, redirect, reverse
from django.db.models import Q
from .models import *
from .forms import RegisterForm

def index(request):
    posts = Post.objects.order_by("-date")
    
    return render(request, "blog/index.html", {"posts": posts})

def posts(request):
    posts = Post.objects.all()
    return render(request, "blog/posts.html", {"posts":posts})

def post(request, id):
    post = Post.objects.get(id=id)
    post.views +=1
    post.save()
    return render(request, "blog/post.html", {"post":post})

def categories(request):
    categories = Category.objects.all()
    return render(request, "blog/categories.html", {"categories":categories})

def category(request, id):
    categories = Category.objects.get(id=id)
    posts = Post.objects.filter(categories=categories)
    content = {"category":categories, "posts":posts}
    return render(request, "blog/category.html", content)

def search(request):
   query = request.GET.get('search')
   search_obj = Post.objects.filter(Q(title__icontains=query))
   return render(request, 'blog/search.html', {'search_obj':search_obj, "query":query}) 

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
            form = RegisterForm()
            return render(request, "blog/register.html", {"form":form})

def comment(request, id):
    post = Post.objects.get(id=id)
    if request.method == "POST":
        comment = post.comment_set.create(
             text = request.Post.get("text")
        )
        if request.user.is_superuser:
            comment.publish=True
            comment.save()
    return redirect(reverse("post_detail", kwargs = {"id":id}))


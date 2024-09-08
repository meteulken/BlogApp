from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Blog, Category

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return render(request, "account/login.html")
    context = {
        "blogs": Blog.objects.filter(is_active=True, is_home=True),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/index.html", context)


def blogs(request):
    if not request.user.is_authenticated:
        return render(request, "account/login.html")
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories" : Category.objects.all()
    }
    return render(request, "blog/blogs.html", context)

def blogs_details(request, slug):
    if not request.user.is_authenticated:
        return render(request, "account/login.html")
    blog = Blog.objects.get(slug=slug)
    return render(request, "blog/blog-details.html", {"blog": blog})


def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories" : Category.objects.all(),
        "selected_category": slug
    }
    return render(request, "blog/blogs.html", context)
from django.shortcuts import render
from .models import Category, Post


def home(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'home.html', context)


def category(request, category_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(category=category_id)
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'home.html', context)


def post(request, post_id):
    categories = Category.objects.all()
    posts = Post.objects.filter(id=post_id)
    context = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'home.html', context)

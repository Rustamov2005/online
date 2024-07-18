from django.shortcuts import render
from .models import Blog, Commints, Categore


def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blog.html', context)


def commints(request):
    commit = Commints.objects.all()
    context = {'commit': commit}
    return render(request, 'commints.html', context)


def categories(request):
    categories = Categore.objects.all()
    context = {'categories': categories}
    return render(request, 'categories.html', context)


def blogdetailviwe(request, id):
    blogs = Blog.objects.all(id=id)
    return render(request, 'single.html', {'blogs': blogs})

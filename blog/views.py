from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog, Commints, Categore
from .forms import BlogForm


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


def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('blog_list')  # 'blog_list' - bloglar ro'yxati sahifasi
    else:
        form = BlogForm()
    return render(request, 'blog/create_blog.html', {'form': form})


def update_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', pk=blog.pk)  # 'blog_detail' - blogning batafsil sahifasi
    else:
        form = BlogForm(instance=blog)
    return render(request, 'blog/update_blog.html', {'form': form})


def delete_blog(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')  # 'blog_list' - bloglar ro'yxati sahifasi
    return render(request, 'blog/delete_blog.html', {'blog': blog})


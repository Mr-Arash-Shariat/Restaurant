from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Tag, Category, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def blog_list(request):
    blog = Blog.objects.all()
    # pagination
    page_number = request.GET.get('page')
    paginator = Paginator(blog, 3)
    objects_list = paginator.get_page(page_number)

    context = {
        'blogs': objects_list
    }

    return render(request, 'blog/blog_list.html', context)


def blog_detail(request, slug):
    blogs = get_object_or_404(Blog, slug=slug)
    tags = Tag.objects.all().filter(blog=blogs)
    recent_blogs = Blog.objects.all().order_by('-created_at')[:3]
    categories = Category.objects.all()
    comments = Comment.objects.all().filter(blog=blogs)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            comment = Comment(blog=blogs, name=name, email=email, message=message)
            comment.save()

    context = {
        'blog': blogs,
        'tags': tags,
        'recent_blogs': recent_blogs,
        'categories': categories,
        'comments': comments,
    }

    return render(request, 'blog/blog_detail.html', context)


def blog_tag(request, tag):
    blog = Blog.objects.filter(tag__slug=tag)

    contaxt = {
        'blogs': blog
    }

    return render(request, 'blog/blog_list.html', contaxt)


def blog_category(request, category):
    blog = Blog.objects.filter(category__slug=category)

    context = {
        'blogs': blog
    }

    return render(request, 'blog/blog_list.html', context)
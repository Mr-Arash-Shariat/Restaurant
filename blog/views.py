from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog, Tag, Category, Comment
from .forms import CommentForm



def blog_list(request):
    blogs = Blog.objects.all()

    context = {
        'blogs': blogs
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
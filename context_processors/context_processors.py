from blog.models import Blog



def recent_blogs(request):
    recent_blog = Blog.objects.order_by('created_at')[:4]

    return {"recent_blogs": recent_blogs}
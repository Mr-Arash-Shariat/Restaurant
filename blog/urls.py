from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('detail/<slug:slug>', views.blog_detail, name='blog_detail'),
    path('', views.blog_list, name='blog_list'),
]
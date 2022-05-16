from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('detail/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('tags/<slug:tag>/', views.blog_tag, name='tags'),
    path('categories/<slug:category>/', views.blog_category, name='categories')
]
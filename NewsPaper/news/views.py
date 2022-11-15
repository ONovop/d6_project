from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

class PostList(ListView):
    model = Post
    ordering = '-time_creating'
    template_name = 'news.html'
    context_object_name = 'posts'

class PostDetail(DetailView):
    model = Post
    template_name = 'news_d.html'
    context_object_name = 'post'

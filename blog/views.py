"""
Used for imports for views.py
"""
from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    class to Post Blog list to view and use templates
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6

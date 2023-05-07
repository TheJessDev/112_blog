from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
)
from .models import Post

class PostListView(ListView):
    template_name = "posts/lists.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/details.html"
    model = Post

class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]
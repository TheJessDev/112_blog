from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LonginRequiredMixin,
    UserPassesTestMixin
)
from .models import Post

class PostListView(ListView):
    template_name = "posts/lists.html"
    model = Post

class PostDetailView(DetailView):
    template_name = "posts/details.html"
    model = Post

class PostCreateView(LoginRequiredMixins, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]
# MIXINS appear LEFT of PARENT always
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixins, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def test_func(self):
        # you can do anthing you want here
        # as long as this returns True or False in the end
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixins, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user 



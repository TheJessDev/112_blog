from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Post, Status

class PostListView(ListView):
        # for published posts
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_list"] = Post.objects
        context["object_list"] = context["post_list"]
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["post_list"] = Post.objects.filter(
            status=draft_status
            ).filter(
            author=self.request.user
            ).order_by("created_on").reverse()
        return context
    
class ArchivedPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/list.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        archived_status = Status.objects.get(name="archived")
        context["post_list"] = Post.objects.filter(
            status=archived_status
        ).order_by("created_on").reverse()
        return context

class PostDetailView(DetailView):
    template_name = "posts/details.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "author", "body"]
# MIXINS appear LEFT of PARENT always
    def form_valid(self, form):
        form.instance.author = self.request.user
        draft_status = Status.objects.get(name="draft")
        form.instance.status = draft_status
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        # you can do anthing you want here
        # as long as this returns True or False in the end
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("list")

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user 



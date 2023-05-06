from django.views.generic import ListView
from django.views.generic import DetailView
from django.views.generic import CreateView
from .models import posts


class ListView(ListView):
    template_name = lists.html
    model = ListView

class DetailView(DetailView):
    template_name = details.html
    model = ListView
    fields = ["title", "author", "date"]

class CreateView(CreateView):
    template_name = create.html
    model = ListView

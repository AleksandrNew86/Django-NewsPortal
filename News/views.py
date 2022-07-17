from django.views.generic import ListView, DetailView
from .models import Post


class NewsList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'News/list_news.html'
    context_object_name = 'news'


class NewsDetail(DetailView):
    model = Post
    template_name = 'News/news.html'
    context_object_name = 'news'




from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class NewsList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'News/list_news.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().queryset()
        self.filterset = PostFilter([self.request.GET, queryset])
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['filterset'] = self.filterset


class NewsDetail(DetailView):
    model = Post
    template_name = 'News/news.html'
    context_object_name = 'news'




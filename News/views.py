
from django.views.generic import ListView, DetailView, CreateView,\
    UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Post
from .filters import PostFilter
from .forms import NewsForm
from django.urls import reverse_lazy


class NewsList(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'News/list_news.html'
    context_object_name = 'news'
    paginate_by = 10


class NewsDetail(DetailView):
    model = Post
    template_name = 'News/news.html'
    context_object_name = 'news'


class NewsSearch(ListView):
    model = Post
    ordering = '-date_creation'
    template_name = 'News/news_search.html'
    context_object_name = 'news'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class NewsCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'News/news_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_post = 'NW'
        return super().form_valid(form)
    permission_required = 'News.add_post'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    form_class = NewsForm
    model = Post
    template_name = 'News/article_create.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.type_post = 'AR'
        return super().form_valid(form)
    permission_required = 'News.add_post'


class NewsEdit(PermissionRequiredMixin, UpdateView):
    form_class = NewsForm
    model = Post
    template_name = 'News/news_edit.html'
    permission_required = 'News.change_post'


class NewsDelete(DeleteView):
    model = Post
    template_name = 'News/news_delete.html'
    success_url = reverse_lazy("news_list")








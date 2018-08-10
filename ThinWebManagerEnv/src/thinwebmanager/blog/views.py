from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
CreateView,
UpdateView,
DetailView,
DeleteView,
ListView
)

from .forms import ArticleForm
from .models import Article


class ArticleCreateView(CreateView):
    template_name = "articles/article_create.html"
    form_class = ArticleForm
    queryset = Article.objects.all()


class ArticleListView(ListView):
    template_name = "articles/articles_list.html"
    queryset = Article.objects.all()


class ArticleDetailView(DetailView):
    template_name = "articles/article_details.html"

    def get_object(self, queryset=None):
        article_id_ = self.kwargs.get("article_id")
        return get_object_or_404(Article, id=article_id_)


class ArticleUpdateView(UpdateView):
    template_name = "articles/article_create.html"
    form_class = ArticleForm

    def get_object(self, queryset=None):
        article_id_ = self.kwargs.get("article_id")
        return get_object_or_404(Article, id=article_id_)


class ArticleDeleteView(DeleteView):
    template_name = "articles/article_delete.html"

    def get_object(self, queryset=None):
        article_id_ = self.kwargs.get("article_id")
        return get_object_or_404(Article, id=article_id_)

    def get_success_url(self):
        return reverse("articles:article-list")
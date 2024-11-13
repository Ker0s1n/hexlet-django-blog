# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View

from hexlet_django_blog.article.models import Article

from .forms import ArticleForm, ArticleCommentForm


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleInfo(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article.objects, id=kwargs["article_id"])
        return render(
            request,
            "articles/info.html",
            context={
                "article": article,
            },
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, 'articles/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles_list')
        return render(request, 'articles/create.html', {'form': form})


class ArticleCommentView(View):
    def get(self, request, *args, **kwargs):
        form = get_object_or_404(ArticleCommentForm(), kwargs["article_id"])
        return render(
            request,
            "articles/comment.html",
            {"form": form}
        )

    def post(self, request, *args, **kwargs):
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            form.save()
            id = kwargs["article_id"]
            return redirect(reverse("articles-info", id))
        return render(request, "articles/comment.html", {"form": form})

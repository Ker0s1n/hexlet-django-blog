# from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.views import View

from hexlet_django_blog.article.models import Article


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:15]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            }
        )


class ArticleInfo(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article.objects, id=kwargs['article_id'])
        return render(
            request,
            "articles/info.html",
            context={
                "article": article,
            }
        )

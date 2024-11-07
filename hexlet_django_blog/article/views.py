# from django.http import HttpResponse
from django.shortcuts import render
from django.views import View


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        return render(
            request,
            "articles/index.html",
            context={
                "title": "Articles",
                "description": ["Here", "we", "have", "articles", "of blog"],
            },
        )


class ArticleInfo(View):
    def get(self, request, article_id, tags, *args, **kwargs):
        return render(
            request, "articles/info.html", context={"article": article_id, "tags": tags}
        )

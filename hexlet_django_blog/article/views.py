from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from django.views.decorators.http import require_POST

from hexlet_django_blog.article.models import Article, Comment

from .forms import ArticleCommentForm, ArticleForm


class ArticleView(View):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()[:5]
        return render(
            request,
            "articles/index.html",
            context={
                "articles": articles,
            },
        )


class ArticleInfo(View):
    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, id=kwargs["article_id"])
        comments = article.comments.filter()
        form = ArticleCommentForm()
        return render(
            request,
            "articles/info.html",
            context={
                "article": article,
                "comments": comments,
                "form": form,
            },
        )


class ArticleFormCreateView(View):
    def get(self, request, *args, **kwargs):
        form = ArticleForm()
        return render(request, "articles/create.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("articles_list")
        return render(request, "articles/create.html", {"form": form})


class ArticleFormEditView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs["article_id"]
        article = Article.objects.get(id=article_id)
        form = ArticleForm(instance=article)
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("article_id")
        article = Article.objects.get(id=article_id)
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Статья успешно обновлена")
            return redirect("articles_list")

        messages.add_message(request, messages.WARNING, "Требуется устранить ошибки")
        return render(
            request, "articles/update.html", {"form": form, "article_id": article_id}
        )


class ArticleFormDeleteView(View):
    def get(self, request, *args, **kwargs):
        article_id = kwargs["article_id"]
        article = Article.objects.get(id=article_id)
        return render(request, "articles/delete.html", {"article": article})

    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("article_id")
        article = Article.objects.get(id=article_id)
        if article:
            article.delete()
            messages.add_message(request, messages.INFO, "Статья успешно удалена")
        return redirect("articles_list")


class ArticleComment(View):
    def post(self, request, *args, **kwargs):
        article_id = kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)
        form = ArticleCommentForm(request.POST)
        if form.is_valid():
            # body = request.POST.get('comment')
            # comment = Comment(article, body)
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
            messages.add_message(
                request, messages.SUCCESS, "Комментарий успешно добавлен"
            )
        else:
            messages.add_message(
                request, messages.WARNING, "Ошибка при добавлении комментария"
            )
        return redirect("article_info", article_id)

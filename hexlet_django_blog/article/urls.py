from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.ArticleView.as_view()),
    path(
        "<str:tags>/<int:article_id>",
        views.ArticleInfo.as_view(),
        name="article_info",
    ),
]

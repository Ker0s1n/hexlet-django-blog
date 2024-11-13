from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.ArticleView.as_view(), name="articles_list"),
    path(
        "<int:article_id>/",
        views.ArticleInfo.as_view(),
        name="article_info",
    ),
    path(
        "create/",
        views.ArticleFormCreateView.as_view(),
        name="article_create"
    ),
    path(
        "<int:article_id>/comment/",
        views.ArticleCommentView.as_view(),
        name="article_comment"
    )
]

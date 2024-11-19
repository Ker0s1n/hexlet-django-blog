from django.urls import path

from hexlet_django_blog.article import views

urlpatterns = [
    path("", views.ArticleView.as_view(), name="articles_list"),
    path(
        "create/",
        views.ArticleFormCreateView.as_view(),
        name="article_create"
    ),
    path(
        "<int:article_id>/edit/",
        views.ArticleFormEditView.as_view(),
        name="article_update"
    ),
    path(
        "<int:article_id>/delete/",
        views.ArticleFormDeleteView.as_view(),
        name="article_delete"
    ),
    path(
        "<int:article_id>/comment/",
        views.ArticleComment.as_view(),
        name="comment_article",
    ),
    path(
        "<int:article_id>/",
        views.ArticleInfo.as_view(),
        name="article_info",
    ),
]

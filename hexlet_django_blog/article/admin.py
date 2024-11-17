from django.contrib import admin
from django.contrib.admin import DateFieldListFilter

# Register your models here.
from .models import Article, Comment


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ["name", "body"]
    list_filter = (("created_at", DateFieldListFilter),)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("article", "body")
    list_filter = ["article"]

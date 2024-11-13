from django import forms
from .models import Article, ArticleComment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]


class ArticleCommentForm(forms.ModelForm):
    class Meta:
        model = ArticleComment
        fields = ['content']

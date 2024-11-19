from django.db import models


# Create your models here.
class Article(models.Model):
    name = models.CharField(max_length=100)  # название статьи
    body = models.TextField()  # тело статьи
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    body = models.TextField()
    article = models.ForeignKey(
        Article, on_delete=models.CASCADE, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.body

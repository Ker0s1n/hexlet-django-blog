from django.views.generic.base import TemplateView
from django.shortcuts import redirect
from django.urls import reverse


def redir(request):
    return redirect(
        reverse("article_info", kwargs={"article_id": 42, "tags": "python"})
    )


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["who"] = "World"
        return context


class AboutView(TemplateView):
    template_name = "about.html"

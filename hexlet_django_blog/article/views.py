# Create your views here.
from django.shortcuts import render


def index(request):
    return render(
        request,
        'articles/index.html',
        context={
            'title': 'Articles',
            'description': ['Here', 'we', 'have', 'articles', 'of blog']
        },
    )

from django.shortcuts import render, get_object_or_404
from .models import Article


def article_detail(request, id):
    article = get_object_or_404(Article, id=id, status=Article.Status.PUBLISHED)
    return render(request, "news/article/list.html", {"article": article})


def article_list(request):
    articles = Article.objects.published()
    return render(request, "news/article/list.html", {"articles": articles})

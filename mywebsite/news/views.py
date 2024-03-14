from django.shortcuts import render, get_object_or_404

from .admin import Article


def article_list(request):
    articles = Article.publish.all()
    return render(request, "news/article/list.hml", {"articles": articles)


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, "news/article/list.hml", {"articles": article)

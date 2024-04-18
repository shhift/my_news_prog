from django.shortcuts import render, get_object_or_404
from .models import Article
from django.core.paginator import Paginator, EmptyPage


def article_detail(request, year, month, day, article_slg):
    article = get_object_or_404(
        Article,
        status=Article.Status.PUBLISHED,
        slug=article_slg,
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )
    return render(request, "news/article/detail.html", {"article": article})


def article_list(request):
    articles = Article.published.all()

    paginator = Paginator(articles, 2)
    page_number = request.GET.get("page", 1)
    try:
        articles = paginator.page(page_number)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    return render(request, "news/article/list.html", {"articles": articles})

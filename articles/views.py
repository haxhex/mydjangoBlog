from django.shortcuts import render, HttpResponse
from . import models

# Create your views here.

def article_list(request):
    # store all objects in Article in articles
    # sort according to date order_by()
    # (-) order discending
    articles = models.Article.objects.all().order_by('-date')
    # access articles from html file by using dict of articles in render
    args = {'articles' : articles}
    return render(request, 'articles/articleslist.html', args)

def article_detail(request, slug):
    # return HttpResponse(slug)
    article = models.Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article' : article})

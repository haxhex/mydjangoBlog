from django.shortcuts import redirect, render, HttpResponse
from . import models
from django.contrib.auth.decorators import login_required
from . import forms

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

# use @ above the function or class for using decorator, name of decorator and () valuse
@login_required(login_url="/accounts/login")
def create_article(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            # save article, save form in db
            # means do not save form in db : commit=False
            # store all form values in instance
            instance = form.save(commit=False)
            # assigned user to the written article
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/create_article.html', {'form' : form})

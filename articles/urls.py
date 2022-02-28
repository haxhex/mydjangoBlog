from django.urls import path, include
from . import views
# . : current path
# <> : variable, capture url in views

app_name = "articles"
urlpatterns = [
    path('', views.article_list, name="list"),
    path('create', views.create_article, name="create"),
    path('<slug>', views.article_detail, name="detail"),
]

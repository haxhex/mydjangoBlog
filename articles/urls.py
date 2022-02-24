from django.urls import path, include
from . import views
# . : current path

urlpatterns = [
    path('', views.article_list)
]

from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# . : current path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.home),
    # if we go to article next urls will be in this path
    path('articles/', include('articles.urls')),
]

urlpatterns += staticfiles_urlpatterns()

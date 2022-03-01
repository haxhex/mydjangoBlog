from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from articles.views import article_list
# . : current path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    # if we go to article next urls will be in this path
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
    path('', article_list),
]

urlpatterns += staticfiles_urlpatterns()
# access address of image via url
urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
from django.db import models

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    # add inthumbnail
    # add in autor
    # this function return name of articles in admin
    def __str__(self):
        return self.title
    # dont show all body of article in articles list just a summary of it

    def snippet(self):
        return self.body[:50] + ' ...'

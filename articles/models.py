from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.urls import reverse


# model for the Article itself
class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    # this cannot be changed by the user as it is automatically added by django
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])


class Comment(models.Model):
    # a comment can have only one article, but not other way around
    article = models.ForeignKey(
        Article,
        on_delete=models.CASCADE,
        related_name='comments'
    )
    comment = models.TextField()
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )


    def __str__(self):
        return self.comment


    def get_absolute_url(self):
        return reverse('article_list')

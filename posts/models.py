from django.db import models
from django.utils import timezone

__author__ = 'Artem Kraynev'


class Post(models.Model):
    """
    Модель поста
    """
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    redactor = models.CharField(max_length=100, null=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    date_of_change = models.DateTimeField(null=True)
    contents_of_post = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'post'


class Comment(models.Model):
    """
    Модель статьи
    """
    post = models.ForeignKey(Post)

    date_of_creation = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=75)
    comment_text = models.TextField()

    path = models.IntegerField(blank=True, editable=False)
    depth = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = 'comment'


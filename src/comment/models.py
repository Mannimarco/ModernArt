from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.utils import timezone

from post.models import Post


class CommentQuerySet(models.QuerySet):

    def stat(self):
        return self.select_related('author')


class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey('post.Post', related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_comments')
    created_date = models.DateTimeField(auto_now_add=True)

    objects = CommentQuerySet.as_manager()

    def __unicode__(self):
        return self.text

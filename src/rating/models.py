from __future__ import unicode_literals

from django.db import models
from django.db.models import IntegerField

from application import settings
from post.models import Post


class Vote(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_votes')
    value = IntegerField()
    post = models.ForeignKey('post.Post', related_name='votes')

    class Meta:
        unique_together = (('author', 'post'),)

    def __str__(self):
        return str(self.value)

from __future__ import unicode_literals

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
from django.utils.timezone import now


class PostQuerySet(models.QuerySet):

    def shown_for(self, user):
        return self.filter(Q(author=user) | Q(is_deleted=False))

    def published(self):
        return self.filter(Q(pub_date__lt=now()))

    def search(self, text):
        return self.filter(Q(title__icontains=text))

    def stat(self):
        return self.select_related('author')\
            .prefetch_related('comments__author')\
            .annotate(comments_count=models.Count('comments'))\
            .annotate(rating_value=models.Sum('votes__value'))


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_posts')
    title = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    # image = models.ImageField(upload_to='images/')
    # encoded_image = models.CharField(max_length=1000000)
    encoded_image = models.TextField()
    is_deleted = models.BooleanField(default=False)
    pub_date = models.DateTimeField(default=timezone.now)

    objects = PostQuerySet.as_manager()

    def get_rating(self):
        votes = self.votes
        return sum(votes.value for votes in votes.all())

    def __str__(self):
        return self.title

    def __unicode__(self):
        return str(self.pk) + ' ' + str(self.title)

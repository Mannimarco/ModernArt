from django.conf.urls import url
from django.views.decorators.csrf import csrf_exempt

import rating.views
from rating.views import PostRatingValueView

urlpatterns = [
    url(r'^vote_up/$', csrf_exempt(rating.views.vote_up), name='vote_up'),
    url(r'^vote_down/$', csrf_exempt(rating.views.vote_down), name='vote_down'),
    url(r'^rating/$', PostRatingValueView.as_view(), name='rating'),
]

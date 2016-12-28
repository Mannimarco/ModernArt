from django.conf.urls import url

import comment.views

urlpatterns = [
    url(r'^new_comment/$', comment.views.new_comment, name='new_comment'),
    url(r'^comments/$', comment.views.comment_list, name='comments'),
]

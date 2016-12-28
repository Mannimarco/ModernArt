"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib.auth.decorators import login_required
from .views import PostAndCommentsView, EditPostView, CreatePostView, EditPostDialogView

urlpatterns = [
    url(r'^(?P<pk>\d+)/$', PostAndCommentsView.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/edit/$', login_required(EditPostView.as_view()), name='edit'),
    url(r'^(?P<pk>\d+)/edit_dialog/$', login_required(EditPostDialogView.as_view()), name='edit_dialog'),
    url(r'^new/$', login_required(CreatePostView.as_view()), name='new_post'),
    url(r'^(?P<pk>\d+)/rating/', include('rating.urls', namespace="rating")),
    url(r'^(?P<pk>\d+)/comment/', include('comment.urls', namespace="comment")),

]

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
import debug_toolbar
from django.conf.urls import url, include
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static

from application import settings
from post.views import PostListView
from rating.views import PostRatings

urlpatterns = [
                  url(r'^i18n/', include('django.conf.urls.i18n')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),
    url(r'^post/', include('post.urls', namespace="post")),
    url(r'^user/', include('core.urls', namespace='user')),
    url(r'^page(?P<page>\d+)/$', PostListView.as_view()),
    url(r'^$', PostListView.as_view(), name='list'),
    url(r'^posts_rating/$', PostRatings.as_view(), name='ratings'),

)
if settings.DEBUG:
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls))
    ]

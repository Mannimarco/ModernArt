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
from django.conf.urls import url

import django.contrib.auth.views
from django.views.generic import CreateView

import core.views
from core.forms import NewUserForm

urlpatterns = [
    url(r'^account/login/$', django.contrib.auth.views.login, name='login'),
    url(r'^account/logout/$', django.contrib.auth.views.logout, name='logout', kwargs={'next_page': '/'}),
    url(r'^account/register/', CreateView.as_view(
        template_name='registration/registration.html',
        form_class=NewUserForm,
        success_url='/'
    ), name='register'),
    url(r'^(?P<pk>\d+)$', core.views.UserProfileView.as_view(), name='user_view'),
    url(r'^edit/$', core.views.UserUpdateView.as_view(), name='user_update'),
    # url(r'^(?P<username>[a-zA-Z0-9_.-]+)$', core.views.user_page, name='user_page'),

]

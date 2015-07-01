"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^intro/index/$', intro_index),
    url(r'^$', blog_index),
    url(r'^blog/$', blog_index),
    url(r'^blog/index/$', blog_index, name = 'blog_index'),
    url(r'^blog/index/(\d+)$', blog_page, name = 'blog_page'),
    url(r'^blog/post/(\d+)$', blog_post, name = 'blog_post'),
    url(r'^blog/about/$', blog_about, name = 'blog_about'),
    url(r'^blog/contact/$', blog_contact, name = 'blog_contact'),
    url(r'^blog/edit_blog/$', edit_blog, name = 'blog_edit_blog'),
    url(r'^blog/login/$', blog_login, name = 'blog_login'),
    url(r'^blog/logout/$', blog_logout, name = 'blog_logout'),
    url(r'^sunny/$', sunny, name = 'sunny'),
]

# -*- coding: UTF-8 -*-
"""myBlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url
from blog import views
from blog import feeds

'''
python manage.py createsuperuser
创建管理员用户:zhguixin Z-gx1991
'''

'''
app_name='blog' 告诉 Django 这个 urls.py 模块是属于 blog 应用的
防止 index、detail等与别的视图函数冲突
'''
#app_name='blog'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    # (?P<pk>[0-9]+)表示命名捕获组，正则匹配的数字会在调用视图函数 detail 时被传递进去
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    # 该分类页由首页跳转，name指定为【kind】，方便在模板中通过url标签找到，但http地址还是【catergory】
    url(r'^category/$', views.kind, name='kind'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^tag/$', views.tag, name='tag'),
    url(r'^about/$', views.about, name='about'),
    url(r'^comment/blog/(?P<blog_pk>[0-9]+)/$', views.blog_comment, name='blog_comment'),
    url(r'^all/rss/$', feeds.AllBlogsRssFeed(), name='rss'),
]

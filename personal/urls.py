# -*- coding: UTF-8 -*-
'''
Created on 2018年1月10日

@author: zhguixin
'''

from django.conf.urls import url
from personal import views

urlpatterns = [
    url(r'^gallery/$', views.gallery, name='gallery'),
    url(r'^register/$', views.register, name='register'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
]
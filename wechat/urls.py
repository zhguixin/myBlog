#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2018年1月26日

@author: zhguixin
'''

from django.conf.urls import url
from wechat import views

urlpatterns = [
    url(r'^$', views.wechat, name='wechat'),
]

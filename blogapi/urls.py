#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2018年10月14日

@author: zhguixin
'''
from django.conf.urls import url, include
from rest_framework import routers
from blogapi import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'blogs', views.BlogViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]

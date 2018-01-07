# -*- coding: UTF-8 -*-
'''
Created on 2018年1月6日

@author: zhguixin
'''
from django import template
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from blog.models import Blog, Catagory, Comment

register = template.Library()

@register.simple_tag
def get_category():
    return Catagory.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)

@register.simple_tag(takes_context=True)
def get_comments_by_blog(context, pk):
    blog = get_object_or_404(Blog, pk=pk)
    return blog.comment_set.all()

if __name__ == '__main__':
    pass
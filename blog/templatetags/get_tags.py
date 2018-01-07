# -*- coding: UTF-8 -*-
'''
Created on 2018年1月6日

@author: zhguixin
'''
from django import template
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from ..models import Tag,Blog

register = template.Library()

# Django 1.9 后才支持 simple_tag 模板标签
@register.simple_tag
def get_tags():
    # Count 计算分类下的文章数，其接受的参数为需要计数的表的名称，不区分大小写
    return Tag.objects.annotate(num_blogs=Count('blog')).filter(num_blogs__gt=0)

@register.simple_tag(takes_context=True)
def get_blogs_by_tag(context, pk):
    tag = get_object_or_404(Tag, pk=pk)
    return Blog.objects.filter(tags=tag).order_by('-created')
    #context['blogs'] = blogs

if __name__ == '__main__':
    pass
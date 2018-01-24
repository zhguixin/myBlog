# -*- coding: UTF-8 -*-
'''
Created on 2018年1月18日

@author: zhguixin
'''
from django import template
from django.shortcuts import get_object_or_404
from django.db.models.aggregates import Count
from personal.models import Image, Category

register = template.Library()

@register.simple_tag
def get_category():
    return Category.objects.annotate(num_blogs=Count('image')).filter(num_blogs__gt=0)

@register.simple_tag(takes_context=True)
def get_images_by_category(context, pk):
    cate = get_object_or_404(Category, pk=pk)
    return Image.objects.filter(category=cate).order_by('-created')

if __name__ == '__main__':
    pass
# -*- coding: UTF-8 -*-
'''
Created on 2018年1月5日

@author: zhguixin
'''

from django import template
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

register = template.Library()

'''
自定义模板标签实现分页功能
模板标签是一系列的python函数，通过入参处理后返回到模板html中
'''
# context对应于当前模板的上下文
# object_list表示未分页的所有博客文章列表
# page_count表示每页几篇文章
# 这个装饰器表明这个函数是一个模板标签
@register.simple_tag(takes_context=True)
def paginate(context, object_list, page_count):
    left = 3 # 当前页前两页显示...
    right = 3 # 当前页后两页显示...

    paginator = Paginator(object_list, page_count)
    page = context['request'].GET.get('page') # 从 Http 请求中获取用户请求的页码号

    try:
        object_list = paginator.page(page)
        context['current_page'] = int(page)
        pages = get_left(context['current_page'], left, paginator.num_pages) + get_right(context['current_page'], right,
                                                                                         paginator.num_pages)
    except PageNotAnInteger:
        object_list = paginator.page(1)
        context['current_page'] = 1
        pages = get_right(context['current_page'], right, paginator.num_pages)
    except EmptyPage:
        object_list = paginator.page(paginator.num_pages)
        context['current_page'] = paginator.num_pages
        pages = get_left(context['current_page'], left, paginator.num_pages)

    context['blogs'] = object_list # 对应重新分页后的列表
    context['pages'] = pages
    context['last_page'] = paginator.num_pages
    context['first_page'] = 1
    try:
        context['pages_first'] = pages[0]
        context['pages_last'] = pages[-1] + 1
    except IndexError:
        context['pages_first'] = 1
        context['pages_last'] = 2

    return ''  # 必须加这个，否则首页会显示个None


def get_left(current_page, left, num_pages):
    if current_page == 1:
        return []
    elif current_page == num_pages:
        l = [i - 1 for i in range(current_page, current_page - left, -1) if i - 1 > 1]
        l.sort()
        return l
    l = [i for i in range(current_page, current_page - left, -1) if i > 1]
    l.sort()
    return l


def get_right(current_page, right, num_pages):
    if current_page == num_pages:
        return []
    return [i + 1 for i in range(current_page, current_page + right - 1) if i < num_pages - 1]


if __name__ == '__main__':
    pass
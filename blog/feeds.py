# -*- coding: UTF-8 -*-
'''
Created on 2018年1月7日

@author: zhguixin
'''

from django.contrib.syndication.views import Feed
from .models import Blog

'''
RSS订阅支持
'''
class AllBlogsRssFeed(Feed):
    # 显示在聚合阅读器上的标题
    title = "GuiXin's Blog"

    # 通过聚合阅读器跳转到网站的地址
    link = "/"

    # 显示在聚合阅读器上的描述信息
    description = "zhguixin的个人博客"

    # 需要显示的内容条目
    def items(self):
        return Blog.objects.all()

    # 聚合器中显示的内容条目的标题
    def item_title(self, item):
        return '[%s] %s' % (item.title, item.abstract)

    # 聚合器中显示的内容条目的描述
    def item_description(self, item):
        return item.content

if __name__ == '__main__':
    pass
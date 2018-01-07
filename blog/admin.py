# -*- coding: UTF-8 -*-

from django.contrib import admin
from .models import *

# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    '''
    BlogAdmin类，继承admin.ModelAdmin父类
    '''
    # 美化Blog界面的显示，以列表的形式显示Blog的标题和时间
    list_display = ('title', 'created')
    # 增加查询功能，在Blog的标题和摘要中查询关键字
    search_fields = ('title', 'abstract')
    # 用在多对多字段上，方便过滤标签
    filter_horizontal = ('tags',)
    # 根据创建日期过滤Blog，由系统提供几种过滤方式：今天、过往七天、当月和今年
    list_filter = ('created',)
    # 更为精确的按照创建日期（降序）过滤Blog，精确到年月日，注意该字段接收的是一个字符串
    date_hierarchy = 'created'
    # 前面的 - 号，指定排序方式按照Blog创建日期的降序方式
    ordering = ('-created',)
    # fields 指定在编辑页面允许被编辑的字段
    # fields = ('title', 'abstract', 'content')
    # raw_id_fields解决外键（对应Blog的Catagory）过多导致加载编辑页面时间过长的问题
    # 使用此项 catagory 字段将被展现成【文本框】 ，而不再是【下拉框】
    # raw_id_fields = ('catagory',)

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Blog, BlogAdmin)
admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Tag, TagAdmin)

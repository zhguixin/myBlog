# -*- coding: UTF-8 -*-
from django.db import models
#from django.urls.base import reverse # Django 1.10版本
from django.core.urlresolvers import reverse # Django 1.9 的版本

'''
各个数据表的关系： 
博客：一篇博客可以有多个标签，多个评论，属于一个分类 
标签：一类标签可以赋予多篇博客，一个博客也可以由多个标签，所以是博客和标签是多对多的关系 
分类：一个分类内部可以有多个博客，我们规定一个博客只对应一个分类，所以博客和分类是一对多的关系 
评论：很明显一个评论属于一个博客，而一个博客可以有很多的评论，所以是博客和评论是一对多的关系。
'''
# Create your models here.
# 注意：这里表的字段名取为【Catagory】,视图函数，模板使用的url则为【Category】
# （感觉自己把自己坑了，两个名字没有去一样）
class Catagory(models.Model):
    """
    博客分类
    """
    name = models.CharField(u'名称',max_length=30)

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk':self.pk})

class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField(u'名称',max_length=16)

    def __unicode__(self):
        return self.name

class Blog(models.Model):
    """
    博客，允许作者为空，摘要为空
    """
    title = models.CharField(u'标题',max_length=32)
    author = models.CharField(u'作者',max_length=16, blank=True)
    abstract = models.CharField(u'摘要',max_length=200, blank=True)
    content = models.TextField(u'博客正文')
    created = models.DateTimeField(u'发布时间',auto_now_add=True)
    catagory = models.ForeignKey(Catagory,verbose_name=u'分类', default= '')
    tags = models.ManyToManyField(Tag,verbose_name=u'标签', default='')

    class Meta:
        ordering = ['-created', 'title']

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        # pk 和 id 是等价的,对应数据库中的id值
        # 第一个参数 blog:detail 的意义表示 blog 应用下的 name=detail 的函数
        return reverse('detail', kwargs={'pk':self.pk})

class Comment(models.Model):
    """
    评论
    """
    blog = models.ForeignKey(Blog,verbose_name=u'博客')
    name = models.CharField(u'称呼',max_length=16)
    email = models.EmailField(u'邮箱')
    content = models.CharField(u'内容',max_length=240)
    created = models.DateTimeField(u'发布时间',auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __unicode__(self):
        return self.name

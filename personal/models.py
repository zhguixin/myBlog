# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from easy_thumbnails.fields import ThumbnailerImageField
from django.core.urlresolvers import reverse

# Create your models here.

# 继承自AbstractUser抽象类,覆写Meta子类
class User(AbstractUser):
    nickname = models.CharField(max_length=50, blank=True)

    class Meta(AbstractUser.Meta):
        pass

@python_2_unicode_compatible
class Category(models.Model):
    """
    照片分类
    """
    name = models.CharField(u'名称',max_length=30)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'pk':self.pk})

@python_2_unicode_compatible
class Image(models.Model):
    '''
    模型包含Title、文件、描述、创建时间、分类
    '''
    title = models.CharField(max_length=250, blank=True)
    original = ThumbnailerImageField(upload_to=settings.IMAGE_PREFIX, default='/tmp/none.jpg')
    description = models.CharField(max_length=400, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,verbose_name=u'分类', default= '')

    def __str__(self):
        return self.title

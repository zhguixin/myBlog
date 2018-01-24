# -*- coding: UTF-8 -*-
from django.contrib import admin
from .models import User, Image, Category

# Register your models here.
# 为了能在 Admin 后台查看用户数据，首先需要注册用户模型
class ImageAdmin(admin.ModelAdmin):
    list_display = ('category',)

admin.site.register(User)
admin.site.register(Image, ImageAdmin)
admin.site.register(Category)

# -*- coding: UTF-8 -*-
'''
Created on 2018年10月14日

@author: zhguixin
'''
from rest_framework import serializers
from blog.models import Blog, Catagory, Tag

class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Catagory
#         fields = '__all__'
        exclude = ['id',]

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
#         fields = '__all__'
        exclude = ['id',]

class BlogSerializer(serializers.ModelSerializer):
    # ForeignKey
    catagory = CatagorySerializer(read_only=True)
    # ManyToManyField
    tags = TagSerializer(many=True, read_only=True)
    class Meta:
        model = Blog
        exclude = ['id', 'author']

# -*- coding: UTF-8 -*-
import os, io
import markdown
from django.utils.text import slugify
from markdown.extensions.toc import TocExtension
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import CommentForm

'''
pip install markdown
pip install Pygments
语法高亮通过：pygmentize -f html -a .codehilite -S default > pygments.css
产生css文件，拷贝到static目录下进行引用
'''
# Create your views here.
def index(request):
    blogs = Blog.objects.all()
    return render(request, 'index.html', {'blogs':blogs})

def detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)
    # 将Markdown渲染为html
    md = markdown.Markdown(extensions=[
                                 'markdown.extensions.extra',
                                 'markdown.extensions.codehilite', # codehilite 是语法高亮拓展
                                 'markdown.extensions.toc', #  toc 则允许我们自动生成目录
                                 TocExtension(slugify=slugify),
                              ])
    blog.content = md.convert(blog.content)
    blog.toc = md.toc

    # 博客详情页加入评论
    form = CommentForm()
    # 该语句等价于：Comment.objects.filter(blog=blog)，获取该blog下的所有评论
    comment_list = blog.comment_set.all()
    # 将博客、表单、评论作为模板变量提供给 detail.html 模板以供渲染
    context = {'blog': blog,
           'form': form,
           'comment_list': comment_list
           }
    return render(request, 'detail.html', context=context)

def kind(request):
    blogs = Blog.objects.all()
    return render(request, 'category.html', {'blogs':blogs})

# 数据库分类对应的表名是：Catagory
def category(request, pk):
    cate = get_object_or_404(Catagory, pk=pk)
    blogs = Blog.objects.filter(catagory=cate)
    return render(request, 'category.html', {'blogs':blogs})

# tag页面通过设置锚点的方式实现页内跳转到指定标签字段
def tag(request):
    return render(request, 'tag.html')

# 关于页面不在新建表了，直接加载本地的md文件
# markdown渲染到html页面无法换行时，可在md文件中点两下空格再换行
def about(request):
    # 获得当前文件所在的父目录
    baseDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    fileName = os.path.join(baseDir, 'static', 'introduction.md')
#     info = {}
    # 由于markdown只能解析Unicode编码的字符流,这里选择【io】包下的open方法指定解码格式
    # 默认【os】包下的open函数，解码出来的是ASCII格式的
    with io.open(fileName, "r", encoding="utf-8") as res:
        info = markdown.markdown(res.read())

    return render(request, 'about.html', {'info':info})

# 该视图函数处理某一篇blog通过表单提交过来的评论，验证合法性并保存到数据库
def blog_comment(request, blog_pk):
    print blog_pk
    blog = get_object_or_404(Blog, pk=blog_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            # 三步走：获取评论数据，关联到对应的Blog上，保存到数据库
            cleaned_data = form.cleaned_data
            cleaned_data['blog'] = blog
            Comment.objects.create(**cleaned_data)
            return redirect(blog)
        else:
            comment_list = blog.comment_set.all()
            md = markdown.Markdown(extensions=[
                             'markdown.extensions.extra',
                             'markdown.extensions.codehilite', # codehilite 是语法高亮拓展
                             'markdown.extensions.toc', #  toc 则允许我们自动生成目录
                             TocExtension(slugify=slugify),
                          ])
            blog.content = md.convert(blog.content)
            blog.toc = md.toc
            context = {'blog': blog,
               'form': form,
               'comment_list': comment_list
               }
            return render(request, 'detail.html', context=context)
    # 非post请求，直接重定向到博客详细页
    return redirect(blog)

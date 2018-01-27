#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
Created on 2018年1月27日

@author: zhguixin
'''
import requests
import re
from pymongo import MongoClient

host = 'http://www.ygdy8.net/html/gndy/dyzz/'
def getMovies(url='index.html'):
    movie_list = []
    result = requests.get(host + url)
    content = result.content
    content = content.decode('gbk','ignore').encode('utf-8')
    movies = re.compile(r'<a href="/html/gndy/dyzz/(.*?)" class="ulink">(.*?)</a>').findall(content)
    next = re.compile(r'<a href=\'(.*?)\'>下一页</a>').findall(content)
    for movie in movies:
        movie_dict = {}
        movie_dict['title'] = movie[1]
        movie_dict['url'] = movie[0]
        movie_list.append(movie_dict)
#     if len(movie_list)<200 and len(next)>0:
#         getMovies(next[0])

    movies = []
    for movie in movie_list:
        movie_dict = {}
        year,tag,title = re.compile(r'(.*?)年(.*?)《(.*?)》.*?').findall(movie['title'])[0]
        movie['year'],movie['tag'],movie['title'] = year,tag,title
        movie['url'] = host + movie['url']

        movie_dict['year'] = movie['year']
        movie_dict['tag'] = movie['tag']
        movie_dict['title'] = movie['title']
        movie_dict['url'] = movie['url']

        movies.append(movie_dict)

    return movies

# 测试使用MongoDB，Django对集成MongoDB支持的不是很好
if __name__ == '__main__':
    # 连接MongoDB数据库，默认端口号为27017
    client = MongoClient('localhost',27017)
    # 切换到 admin 数据库进行用户验证
    db_auth = client.admin  
    db_auth.authenticate("zgx", "zhguixin") 
    # 获取 movies 数据库,没有就创建
    db=client.movies
    print db.collection_names()
    # 获取 dytt 集合，没有就创建，后续通过 collection 来操作
    collection=db.dytt
#     collection.insert({'name':'zgx','age':25,'addr':'China'})
    movies = getMovies()
    collection.insert(movies)
#     print movies[0]

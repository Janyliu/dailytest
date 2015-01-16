#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-16'
'''
import urllib

def get_handlernumbers(list_content):
   dict_handler={}
   for dict_single_access in list_content:
       handler_name=dict_single_access['handler']
       dict_handler[handler_name]=dict_handler.get(handler_name,0)+1
   return dict_handler

def get_top(dict_handler_number,top_number):
    sorted_handler=sorted(dict_handler_number.iteritems(),key=lambda d:d[1],reverse=True)
    handler_top=sorted_handler[0:top_number]
    return handler_top


url='https://log.tan14.cn/mongo/apilogs.json'
web_page=urllib.urlopen(url)
content=web_page.read()
list_content=eval(content)
top_number=10
''' 获得接口名以及其所对应的访问次数，字典形式'''
dict_handler_number=get_handlernumbers(list_content)
'''得到给定前几名访问量的接口名称及其访问量，列表形式'''
handler_top=get_top(dict_handler_number,top_number)
for handler in handler_top:
    print handler

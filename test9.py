#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-15'
'''
import urllib

def get_methodhandlernumbers(list_content):
   dict_method_handler_number={}
   for dict_single_access in list_content:
       handler_name=dict_single_access['handler']
       method_name=dict_single_access['method']
       if dict_method_handler_number.get(method_name):
           pass
       else:
           dict_method_handler_number[method_name]={}
       dict_method_handler_number[method_name][handler_name]=dict_method_handler_number[method_name].get(handler_name,0)+1
   return dict_method_handler_number

def get_top(dict_handler_number,top_number):

    sorted_handler=sorted(dict_handler_number.iteritems(),key=lambda d:d[1],reverse=True)
    handler_top=sorted_handler[0:top_number]
    return handler_top


url='https://log.tan14.cn/mongo/apilogs.json'
web_page=urllib.urlopen(url)
content=web_page.read()
list_content=eval(content)
top_number=10
''' 获得方法名、接口名以及其所对应的访问次数，字典形式'''
dict_method_handler_number=get_methodhandlernumbers(list_content)
'''得到以method为标准前10名访问量的接口名称及其访问量，列表形式'''
#print dict_method_handler_number
for method,dict_handler_number in dict_method_handler_number.items():
     print '%s方法下接口访问量前十的为：' %method
     handler_top=get_top(dict_handler_number,top_number)
     for handler in handler_top:
         print handler
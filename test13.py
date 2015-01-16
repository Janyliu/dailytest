#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-16'
'''
import urllib
import time
import string

def get_starttime(start_time):
   m_second=string.atof(start_time)
   second=m_second/1000
   start_time=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(second))
   return start_time

def get_maxtime(last_time,now_time):
   if last_time>=now_time:
       return last_time
   else:
       return now_time


def get_handlertime(list_content):
   dict_method_handler_time={}
   for dict_single_access in list_content:
       method_name=dict_single_access['method']
       handler_name=dict_single_access['handler']
       #user_name=dict_single_access['login_email']
       start_time=get_starttime(dict_single_access['start_time'])
       dict_method_handler_time[method_name]=dict_method_handler_time.get(method_name,{})
       if dict_method_handler_time[method_name].get(handler_name):
           this_request_time=get_maxtime(dict_single_access['request_time'],dict_method_handler_time[method_name][handler_name][0])
           list_time=(this_request_time,start_time)
           dict_method_handler_time[method_name][handler_name]=list_time
       else:
           dict_method_handler_time[method_name][handler_name]=(dict_single_access['request_time'],start_time)
   return dict_method_handler_time


def get_top(dict_handler_time,top_number):
    sorted_handler = sorted(dict_handler_time.iteritems(),key=lambda d:string.atof(d[1][0]),reverse = True)
    handler_top=sorted_handler[0:top_number]
    return handler_top


url='https://log.tan14.cn/mongo/apilogs.json'
web_page=urllib.urlopen(url)
content=web_page.read()
list_content=eval(content)
top_number=10
''' 获得接口名以及其所对应的响应时间,开始时间，字典形式'''
dict_method_handler_time=get_handlertime(list_content)
'''得到给定方法前几名访问量的不重复的接口名称及其时间，列表形式'''
for method,dict_handler_time in dict_method_handler_time.items():
    print '%s方法下接口响应时间最长前十的为：' %method
    handler_top=get_top(dict_handler_time,top_number)
    for handler in handler_top:
       print handler

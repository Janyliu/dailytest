#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-16'
'''
import urllib2

def get_dict(list_content):
    dict_method={}
    for dict_single_access in list_content:
        method_name=dict_single_access['method']
        handler_name=dict_single_access['handler']
        user_name=dict_single_access['login_email']
        del dict_single_access['method']
        del dict_single_access['handler']
        del dict_single_access['login_email']
        dict_method[method_name]=dict_method.get(method_name,{})
        dict_method[method_name][handler_name]=dict_method[method_name].get(handler_name,{})
        dict_method[method_name][handler_name][user_name]=dict_method[method_name][handler_name].get(user_name,[])
        dict_method[method_name][handler_name][user_name].append(dict_single_access)
    return dict_method

def get_handler_top(dict,top_handler_number):
    sorted_dict=sorted(dict.items(),key=lambda d:(sum(len(d[handler][user]))for handler in d for user in d[handler]),reverse=True)
    handler_top=sorted_dict[0:top_handler_number]
    return handler_top

def get_user_top(dict,top_user_number):
    sorted_dict=sorted(dict.keys(),key=lambda d:(len(d[user])for user in d),reverse=True)
    user_top=sorted_dict[0:top_user_number]
    return user_top

url='https://log.tan14.cn/mongo/apilogs.json'
web_page=urllib2.urlopen(url)
content=web_page.read()
list_content=eval(content)
top_handler_number=10
top_user_number=3
dict_method_handler_user=get_dict(list_content)
for method,dict_handler_user in dict_method_handler_user.items():
    print '%s方法下，访问量前十名的接口为：' %method
    handler_top=get_handler_top(dict_handler_user,top_handler_number)
    for handler in handler_top:
       print handler[0]
       print '  前三用户为：'
       user_top=get_user_top(handler[1],top_user_number)
       for user in user_top:
           print '    ',user
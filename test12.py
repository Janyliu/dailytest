#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-16'
'''
import urllib
import time
import string

'''
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
'''

def get_handlernumbers(list_content):
   dict_handler={}
   dict_handler_user={}
   for dict_single_access in list_content:
       handler_name=dict_single_access['handler']
       dict_handler[handler_name]=dict_handler.get(handler_name,0)+1
       user_name=dict_single_access['login_email']
       dict_handler_user[handler_name]=dict_handler_user.get(handler_name,{})
       dict_handler_user[handler_name][user_name]=dict_handler_user[handler_name].get(user_name,0)+1
   return dict_handler,dict_handler_user

def get_top(dict,top_number):
    sorted_handler=sorted(dict.iteritems(),key=lambda d:d[1],reverse=True)
    top=sorted_handler[0:top_number]
    return top

'''
def get_top2(dict,top_number):
    sorted_handler = sorted(dict.iteritems(),key=lambda d:string.atof(d[1][0]),reverse = True)
    top=sorted_handler[0:top_number]
    return top
'''

def handler_number(list_content,top_handler_number,top_user_number):
    dict_handler_number,dict_handler_user_number=get_handlernumbers(list_content)
    handler_top=get_top(dict_handler_number,top_handler_number)
    for handler in handler_top:
        print handler
        user_top=get_top(dict_handler_user_number[handler[0]],top_user_number)
        for user in user_top:
            print '    ',user

def method_handler_number(list_content,top_handler_number,top_user_number):
    pass

def handler_time(list_content,top_handler_number,top_user_number):
    pass

def method_handler_time(list_content,top_handler_number,top_user_number):
    pass


dict_question={'1':u'接口调用次数前10的接口及相应次数(不区分method),每个接口中调用次数前三的用户及其次数',
               '2':u'分method 接口调用次数前10的接口及相应次数,每个接口中调用次数前三的用户及其次数',
               '3':u'接口响应时间最长的前10个接口(不重复的10个）及其响应时长，开始时间(不区分method),每个接口中调用次数前三的用户及其次数',
               '4':u'分 method 接口响应时间最长的前10个接口(不重复的10个）及其响应时长，开始时间,每个接口中调用次数前三的用户及其次数'}
for number,question in dict_question.items():
    print number,question
print '请输入您的问题1,2,3or4:'
select_question=raw_input()
url='https://log.tan14.cn/mongo/apilogs.json'
web_page=urllib.urlopen(url)
content=web_page.read()
list_content=eval(content)
top_handler_number=10
top_user_number=3
dict_solution={'1':handler_number(list_content,top_handler_number,top_user_number),
               '2':method_handler_number(list_content,top_handler_number,top_user_number),
               '3':handler_time(list_content,top_handler_number,top_user_number),
               '4':method_handler_time(list_content,top_handler_number,top_user_number)}
dict_solution.get(select_question)

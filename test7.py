#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-16'
'''
import os

lists=[]

class Empty_file(Exception):
    def __init__(self):
        Exception.__init__(self)
def getfiles(root,format):
    for now_root,dirs,files in os.walk(root):

        if len(files)!=0:
            for now_file in files:

                now_format=now_file.split('.')[-1]
                if now_format==format:
                   now_list=os.path.join(now_root,now_file)
                   lists.append(now_list)

def get_linenumbers(now_file):
    line_blank=line_comment=line_code=0
    lines = False
    try:
        lines=open(now_file)
        if len(open(now_file).read())==0:
            raise Empty_file()
        else:
            for line in lines:
                line = line.lstrip()
                if not line:
                    line_blank +=1
                elif line[0]=='#':
                    line_comment +=1
                else:
                    line_code +=1

            line_total=line_blank+line_comment+line_code
            linenumber=[line_blank,line_comment,line_code,line_total]
        return linenumber
    except IOError:
        print 'IOError!'
        return False
    except Empty_file:
        print 'Empty_file!!'
        return False
    finally:
        if lines:
            lines.close()

getfiles('/home/z/workspace/mcaccount/','py')
print 'Python文件的个数:',len(lists)
print '文件名：空行数 注释行数 代码行数 总行数'
for now_file in lists:
    linenumbers=get_linenumbers(now_file)
    print now_file,linenumbers
#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
  author = 'z'
  date = '15-1-14'
'''

lists=[]

class Empty_file(Exception):
    def __init__(self):
        Exception.__init__(self)

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
            linenumber = [line_blank,line_comment,line_code,line_total]
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



linenumbers=get_linenumbers('/home/z/桌面/y')
print linenumbers
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-25 23:31:25
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 4.1 遍历整个列表
print("4.1")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)


# 4.1.1 深入的研究循环
print("4.1.1")

# 4.1.2 在for循环中执行更多的操作
# 4.1.3 在for循环结束后执行一些操作
print("4.1.2")
print("4.1.3")
magicians = ['alice', 'david', 'carolina'] 
for magician in magicians: 
    print(magician.title() + ", that was a great trick!")  
    print("I can't wait to see your next trick, " + magician.title() + ".\n") 
    
print("Thank you everyone, that was a great magic show!")

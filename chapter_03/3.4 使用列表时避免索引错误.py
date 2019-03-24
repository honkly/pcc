#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-04-01 09:12:44
# @Author  : honkly (honkly@163.com)
# @Link    : http://http://www.cnblogs.com/honkly/
# @Version : $Id$

#3.4 使用列表时避免索引错误

motorcycles = ['honda','yamaha','suzuki']

#print(motorcycles[3])
print(motorcycles[-1])

motorcycles = []
#print(motorcycles[-1])

print("------动手试一试------")

# 3-11 有意引发错误：
print("3-11")
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[3])
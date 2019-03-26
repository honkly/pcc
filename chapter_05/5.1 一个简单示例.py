#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 00:05:09
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 5.1 一个简单示例
print("5.1")

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

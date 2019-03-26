#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-26 23:27:08
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 4.5 元组
# 4.5.1 定义元组
print("4.5.1")
dimensions = (200,50)
print(dimensions[0])
print(dimensions[1])

# 4.5.2 遍历元组中的所有值
print("4.5.2")

print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
# 4.5.3 修改元组变量
print("4.5.3")

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

print("------动手试一试------")

# 4-13 自助餐
print("4-13")

print("打印五种食品")
foods = ('noodle', 'bread', 'cookie', 'dumplings', 'tofu')
for food in foods:
	print(food)

# foods[0] = 'Baozi'

print("\n新菜单")
foods = ('noodle', 'bread')
for food in foods:
	print(food)

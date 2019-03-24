#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-28 22:23:51
# @Author  : honkly (honkly@163.com)
# @Link    : http://http://www.cnblogs.com/honkly/
# @Version : 1.0

# 3.1 列表是什么
print("3.1")

bicycles = ['trek','cannondale','redline','specialized']
print(bicycles)

# 3.1.1 访问列表元素
print("3.1.1")
print(bicycles[0])
print(bicycles[0].title())

# 3.1.2 索引从0而不是1开始
print("3.1.2")

print(bicycles[1],bicycles[3])

print(bicycles[-1])

# 3.1.3 使用列表中的各个值
print("3.1.3")

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

print("------动手试一试------")

# 3.1 姓名
print("3.1")
names = ['honkly','kevin','YongLee','Bernard']
for name in names:
	print(name)

# 3.2 问候语
print("3.2")
for name in names:
	print("Hi!" + name.title()+"!")

# 3.3 自己的列表
print("3.3")

road_way = ["bike","train"]
print("I like to ride",road_way[0].title(),"and I am not want to take",road_way[1].title(),"!")
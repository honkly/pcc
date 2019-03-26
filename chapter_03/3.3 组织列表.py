#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-29 23:17:50
# @Author  : honkly (honkly@163.com)
# @Link    : http://http://www.cnblogs.com/honkly/
# @Version : 1.0

# 3.3 组织列表
print("3.3")

# 3.3.1 使用方法sort()对列表进行永久性排序
print("3.3.1")

cars = ['bmw','audi','toyota','subaru']
cars.sort()
print(cars)
cars.sort(reverse =  True)
print(cars)

# 3.3.2 使用函数sorted()对列表进行临时排序
print("3.3.2")

cars = ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
# 如果要按字母顺序相反的顺序显示列表，也可以像函数sorted()传递参数reverse = True
print(sorted(cars,reverse = True))

# 3.3.3 倒着打印列表
print("3.3.3")

# 方法reserse()永久性的修改列表元素的排列顺序，但可以随时再次调用恢复原来的顺序
cars = ['bmw','audi','toyota','subaru']
print(cars)
cars.reverse()
print(cars)

# 3.3.4 确定列表的长度
print("3.3.4")
print(len(cars))

print("------动手试一试------")

# 3-8 放眼世界：
print("3-8")

# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的
area = ['shagnhai','beijing','chengdu','xianggang','taiwan']

# 按原始排列顺序打印该列表
print("#按原始排列顺序打印该列表")
print(area)

# 使用sorted()按字母顺序打印这个列表，同时不要修改它
print("#使用sorted()按字母顺序打印这个列表，同时不要修改它")
print(sorted(area))

# 再次打印该列表，核实排列顺序未改变
print("#再次打印该列表，核实排列顺序未改变")
print(area)

# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它
print("#使用sorted()按与字母顺序相反的顺序打印这个列表，同时不要修改它")
print(sorted(area,reverse = True))

# 再次打印该列表，核实排列顺序未改变
print("#再次打印该列表，核实排列顺序未改变")
print(area)

# 使用reverse()修改列表元素的排列顺序
print("#使用reverse()修改列表元素的排列顺序")
area.reverse()
print(area)

# 使用reverse()再次修改列表元素的排列顺序
print("#使用reverse()再次修改列表元素的排列顺序")
area.reverse()
print(area)

# 使用sort()修改该列表，使其元素按字母顺序排列
print("#使用sort()修改该列表，使其元素按字母顺序排列")
area.sort()
print(area)

# 使用sort()修改该列表，使其元素按字母顺序相反的顺序排列
print("#使用sort()修改该列表，使其元素按字母顺序相反的顺序排列")
area.sort(reverse = True)
print(area)

# 3-9 晚餐嘉宾
names = ['john','lilei','obama']
guest_numbers = len(names)
print("I have invite",guest_numbers,"people to my dinner")
print("I have invite " + str(guest_numbers) + " people to my dinner")

# 3-10 尝试使用各个函数

goods = ['football','obama','xianggang','plan','bicycle']

# 输出此List
print("# 输出此List")
print(goods)

# 首字母大写
print("# 首字母大写")
print(goods[0].title())

# 输出倒数第一个字母
print("# 输出倒数第一个字母")
print(goods[-1])

# 修改列表中的元素
print("# 修改第一个元素")
goods[0] = 'basketball'
print(goods)

# 在列表中添加元素
print("# 末尾添加元素")
goods.append('train')
print(goods)

# 在列表中插入元素
print("# 在列表中插入元素")
goods.insert(0,'HaHa')
print(goods)

# 在列表中删除元素
print("# 在列表中删除元素")
del goods[0]
print(goods)

# 删除元素并打印出来
print("# 删除元素并打印出来")
popped_goods = goods.pop()
print(popped_goods)
print(goods)

# 用pop删除指定元素
print("# 用pop删除指定元素")
popped_goods_2 = goods.pop(0)
print(popped_goods_2)
print(goods)

# 根据值来删除元素
print("# 根据值来删除元素")
goods.remove('plan')
print(goods)

# 使用sort()来排序
print("#使用sort()来排序")
print(goods)

goods_copy = goods
goods_copy.sort()
print(goods_copy)
goods_copy.sort(reverse = True)
print(goods_copy)

# 使用sorted()来排序
print("\n#使用sorted()来排序", ...)

goods = ['xianggang', 'obama', 'bicycle']
print(goods)
print(sorted(goods))
print(sorted(goods,reverse = True))
print(goods)

# 倒着打印列表
print("# 倒着打印列表")
print(goods)
goods.reverse()
print(goods)
print(len(goods))

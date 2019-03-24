#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-28 22:43:15
# @Author  : honkly (honkly@163.com)
# @Link    : http://http://www.cnblogs.com/honkly/
# @Version : 1.0

# 3.2 修改、添加和删除元素
print("3.2")

# 3.2.1 修改列表元素
print("3.2.1")

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

# 3.2.2 在列表中添加元素
print("3.2.2")

# 1. 在列表末尾添加元素
print("1.")

print(motorcycles)
motorcycles.append('plan')
print(motorcycles)

motorcycles_test = []
motorcycles_test.append('ducati')
motorcycles_test.append('yamaha')
motorcycles_test.append('suzuki')
motorcycles_test.append('plan')
print(motorcycles_test)

# 2.在列表中插入元素
print("2.")

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'fly')
print(motorcycles)

# 3.2.3：从列表中删除元素
print("3.2.3")

# 1. 使用del语句删除元素
print("1.")

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[0]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

# 2.使用方法pop()删除元素
print("2.")

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
last_ownd = motorcycles.pop()
print("The last motorcycle I owned was a " + last_ownd.title() + ".")

# 3. 弹出列表中任何位置处的元素
print("3.")

motorcycles = ['honda','yamaha','suzuki']

first_owned = motorcycles.pop(0)
print('The first motorcycles I ownd was a ' + first_owned.title() + '.')

# 如果要从列表中删除一个元素，并且不再以任何方式使用它，就是用del语句
# 如果你要在删除元素后还能继续使用它，就使用方法pop()

# 4. 根据值删除元素
print("4.")

motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki','ducati']
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive.title() + "is too expensive for me.")

# !!!remove()只删除第一个指定的值，被删除的值可能在列表中出现多次，就需要使用循环来判断是否删除了所有这样的值。

print("#------动手试一试------")

# 3-4:嘉宾名单
print("3-4")

names = ['john','lilei','obama']
print("I would invite " + names[0].title() + " 、 " + names[1].title() + " and " + names[2].title() + " to my party!")

# 3-5 修改嘉宾名单
print("3-5")

print(names[2] + " can't go here.")

# 三种方式删除obama:
del names[2]
#names.pop(2)
#names.remove('obama')

names.append('makaien')

print(names)
for name in names:
	print("Welcome!",name,"!")

# 3-6 添加嘉宾
print("3-6")

#你刚找到了一个更大的餐桌
print("I got a bigger desk!")
print(names)

#使用insert()将一位新嘉宾添加到名单开头
names.insert(0, 'Linux')
print(names)

#使用insert()将一位新嘉宾添加到名单中间
names.insert(2,'HaHa')
print(names)

#使用apppend()将最后一位新嘉宾添加到名单末尾
names.append('KaKa')
print(names)

#打印一系列消息，向名单中的每位嘉宾发出邀请。
for name in names:
	print("Welcom to here! " + name + "!")

# 3-7 缩减名单
print("3-7")

# 只能邀请两位嘉宾共进晚餐
print("Only 2 can come here!")

# 使用pop()不断的删除名单中的嘉宾，直到只有2位嘉宾为止
print(names)
number_list = len(names)
print("There are " + str(number_list) + " peoples in the list")

names.pop()
names.pop()
names.pop()
names.pop()

print(names)

# 对于余下的两位嘉宾中的每一位，都打印一条消息，指出他仍然在受邀人之列
for name in names:
	print("Hi " + name + "!","You are still in the list of peopeo")

# 使用del将最后2位嘉宾从名单中删除，让名单变成空的。打印该名单，核实程序结束时名单确实是空的。
names.pop()
names.pop()
print(names)

if names == []:
	print("Delete Already Ok!")
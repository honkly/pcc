#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-26 22:56:32
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 4.4.1 切片
print("4.4.1")

players = ['charles', 'martina', 'michael', 'florence', 'eli'] 

# 提取第2~4个元素
print(players[1:4])

# 提取第1~4个元素
print(players[0:4])
print(players[:4])

# 提取第3个到末尾的元素
print(players[2:])

# 提取最后三个元素
print(players[-3:])

# 4.4.3 复制列表
print("4.4.3")
my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:] 
print(my_foods)
print(friend_foods)

my_foods.append('cannoli') 
friend_foods.append('ice cream') 

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

print("------动手试一试------")
# 4-10 切片
print("4-10")
my_foods = ['pizza', 'noodle', 'bread', 'falafel', 'carrot cake'] 
print("The first three items in the list are:")
print(my_foods[:3])

print("Three items from the middle of the list are:")
print(my_foods[1:4])

print("The last three items in the list are:")
print(my_foods[-3:])

# 4.11 你的比萨和我的比萨
print("4.11")

my_pizzas = ['baozi', 'mantou', 'shuijiao']
friend_pizzas = my_pizzas[:]
my_pizzas.append('noodle')
friend_pizzas.append('bread')
print("My favorite pizzas are:", my_pizzas)
print("My friend's favorite pizzas are:", friend_pizzas)

# 4-12 使用多个循环
print("4-12")
foods = ['pizza', 'noodle', 'bread', 'falafel', 'carrot cake']

for food in foods[:3]:
	print("\n",food)
for food in foods[-2:]:
	print("\n",food)
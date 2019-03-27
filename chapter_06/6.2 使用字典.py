#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 23:48:05
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 6.2 使用字典
print("6.2")

# 6.2.1 访问字典中的值
print("6.2.1")

alien_0 = {'color':'green','points':5}
new_points = alien_0['points']

print("You just earned " + str(new_points) + " points!")

# 6.2.2 添加键值对
print("6.2.2")

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

# 6.2.3 先创建一个空字典
print("6.2.3")

alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(alien_0)

# 6.2.4 修改字典中的值
print("6.2.4")

print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x_position: " + str(alien_0['x_position']))

# 向右移动外星人
# 据外星人当前速度决定将其移动多远
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New position: " + str(alien_0['x_position']))

# 6.2.5 删除键值对
print("6.2.5")

alien_0 = {'color':'green','points':5}
del alien_0['points']
print(alien_0)

# 6.2.6 由类似对象组成的字典
print("6.2.6")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

# 演示如何将较长的print语句分成多行
print("jen's favorite language is " + 
    favorite_languages['jen'].title() + 
    ".")

print("------动手试一试------")

# 6-1 人
print("6-1")

friend = {'first_name': 'Lee', 'last_name': 'Knight', 'age': 27, 'city': 'Beijing'}
for key,value in friend.items():
    print(key,":",value)

print(friend)

# 6-2 喜欢的数字
print("6-2")

favorite_number = {'honkly': 8, 'Knight': 9, 'Lee': 10}
for key,value in favorite_number.items():
    print("Hi! " + key + "! " + "Your favorite number is " + str(value))

# 6-3 词汇表
print("6-3")

words = {'print': 'print words', 'input': 'input words'}
for key,value in words.items():
    print(key + ":" + value)

for key,value in words.items():
    print(key + ":\n\t" + value)




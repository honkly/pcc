#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 21:30:49
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 5.3 if语句
# 5.3.1 简单的if语句
print("5.3.1")

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

# 5.3.2 if-else语句
print("5.3.2")

age = 17
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are too young to vote.")
    print("Please register to vote as soon as you turn 18!")

# 5.3.3 if-elif-else语句
print("5.3.3")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $5.")
else:
    print("Your admission cost is $10")

# 5.3.4 使用多个elif代码块
age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
else:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# 5.3.5 省略else代码块
print("5.3.5")

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 5
elif age < 65:
    price = 10
elif age >= 65:
    price = 5

print("Your admission cost is $" + str(price) + ".")

# 5.3.6 测试多个条件
print("5.3.6")

request_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in request_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in request_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in request_toppings:
    print("Adding extra cheese.")

print("------动手试一试------")

# 5-3 外星人颜色#1：
print("5-3")

alien_color = 'yellow'

if alien_color == 'green':
    print("green,You get 5 points!")

if alien_color == 'yellow':
    print("yellow,You get 5 points!")

# 5-4 外形人颜色#2
print("5-4")

alien_color = 'yellow'
if alien_color == 'green':
    print("green,You get 5 points!")
else:
    print("You get 10 points!")

# 5-5 外形人颜色#3
print("5-5")

alien_color = 'green'
if alien_color == 'yellow':
    print("You get 5 points!")
elif alien_color == 'green':
    print("You get 10 points!")
elif alien_color == 'red':
    print("You get 15 points!")

# 5-6 人生的不同阶段
print("5-6")

age = 27

if age < 2:
    print("He is a baby!")
elif age >= 2 and age < 4:
    print("He is learning to walk!")
elif age >= 4 and age < 13:
    print("He is a children!")
elif age >= 13 and age < 20:
    print("He is a teenager!")
elif age >= 20 and age < 65:
    print("He is a adult!")
elif age >= 65:
    print("Hi is a old!")

# 5-7 喜欢的水果
print("5-7")

favorite_fruits = ['apple', 'orange', 'pear']

if 'apple' in favorite_fruits:
    print("You really like apple!")
if 'orange' in favorite_fruits:
    print("You really like orange!")
if 'pear' in favorite_fruits:
    print("You really like pear!")
if 'banana' in favorite_fruits:
    print("You really lie bananas!")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-29 00:08:13
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 7.2 while循环简介
print("7.2")

# 7.2.1 使用while循环
print("7.2.1")

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

# 7.2.2 让用户选择何时退出
print("7.2.2")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message.lower() != 'quit':
    message = input(prompt)
    if message.lower() != 'quit':
        print(message)

active = True
while active:
    message = input(prompt)
    
    if message.lower() == 'quit':
        active = False
    else:
        print(message)

# 7.2.4 使用break退出循环
print("7.2.4")

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# 7.2.5 在循环中使用continue
print("7.2.5")

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue

    print(current_number)

print("------动手试一试------")

# 7-4 比萨配料
print("7-4")

active =  True
while active:
    food = input("请输入配料(输入quit结束)：")
    if food == 'quit':
        break
    print("I will add " + food + " to foods!")

# 7-5 电影票
print("7-5")

while active:
    age = input("Please input your age:")
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("Your price is free!")
    elif age >=3 and age <= 12:
        print("Your price is 10$!")
    elif age > 12:
        print("Your price is 15$!")

# 7-6 三个出口
print("7-6")

print("同7-4")

# 7-7 无限循环
print("7-7")

# while True:
#     print("Hello world!")
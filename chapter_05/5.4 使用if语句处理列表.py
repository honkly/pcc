#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 22:13:13
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 5.4 使用if语句处理列表
print("5.4")

# 5.4.1 检查特殊元素
print("5.4.1")

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'mushrooms':
        print("Sorry, we are out of mushrooms right now.")
    else:
        print("Adding " + requested_topping + ".")

# 5.4.2 确实列表不是空的
print("5.4.2")

requested_toppings = []
if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

# 5.4.3 使用多个列表
print("5.4.3")

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
        
print("\nFinished making your pizza!")

print("------动手试一试------")

# 5-8 以特殊方式跟管理员打招呼
print("5-8")

users = ['honkly', 'honk', 'admin', 'root']
for user in users:
    if user == 'admin':
        print("Hello admin,would you like to see a status report?")
    else:
        print("Hellow " + user + ",thank you for logging in again")

# 5-9 处理没有用户的情形
print("5-9")

users = []
if users:
    for user in users:
        if user == 'admin':
            print("Hello admin,would you like to see a status report?")
        else:
            print("Hellow " + user + ",thank you for logging in again")
else:
    print("We need to find some users!")

# 5-10 检查用户名
print("5-10")

current_users = ['honkly', 'honk', 'admin', 'root', 'kevin']
new_users = ['honk', 'haha', 'amlogic', 'root', 'inspur']
for new_user in new_users:
    if new_user.lower() in current_users:
        print("You should think another name!")
    else:
        print("This name still not used!")

# 5-11 序数
print("5-11")

number_list = [1,2,3,4,5,6,7,8,9]
for number in number_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")
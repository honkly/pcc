#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 23:48:55
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

message = input("Tell me something, and I will repeat it back to you:")
print(message)

# 7.1.1 编写清晰的程序
print("7.1.1")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nwhat is your first name? "

name = input(prompt)
print("\nHello, " + name + "!")

# 7.1.2 使用int()来获取数值输入
print("7.1.2")

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

# 7.1.3 求模运算符
print("7.1.3")

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print("\nThe number " + str(number) + " is even.")
else:
    print("\nThe number " + str(number) + " is odd.")

print("------动手试一试------")

# 7-1 汽车租赁
print("7-1")

car = input("What car do you need? ")
print("Let me see if I can find you a " + car)

# 7-2 参观定位
print("7-2")

number = input("How many people?")
number = int(number)

if number > 8:
    print("Get out!")
else:
    print("Welcome!")

# 7-3 10的整倍数
print("7-3")

number =  input("Please input a number,and I will tell you if this number is an integral multiple of 10.")
number = int(number)

if number % 10 == 0:
    print("Yes!")
else:
    print("No!")
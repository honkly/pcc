#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-03-26 18:33:11
# @Author  : honkly (liyongoffice@gmail.com)
# @Link    : www.liyongoffice.cn
# @Version : 1.0

# 2.3 字符串
print("2.3")

"This is a string."
'This is also a string.'
'I told my friend,"Python is my favorite language!"'
"The language 'python' is named after monty Python,not the snake."
"One of Python's strengths is its diverse and supportive comunity."

# 2.3.1 使用方法修改字符串的大小写
print("2.3.1") 

# name.py
name = "ada lovelace"
print(name.title())
print(name.upper())
print(name.lower())

# 2.3.2 合并（拼接）字符串
print("2.3.2")

first_name = "ada"
last_name = "lovelace"
# 合并
full_name = first_name + " " + last_name
print(full_name)

print("Hello," + full_name.title() + "!")

message = "Hello," + full_name.title() + "!"
print(message)

# 2.3.3 使用制表符或换行符赖添加空白
print("2.3.3")

print("Python")
print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

# 2.3.4 删除空白
print("2.3.4")
favorite_language = ' Python '
print(len(favorite_language))
l = favorite_language.rstrip()  #删除右边空格
m = favorite_language.lstrip()  #删除左边空格
n = favorite_language.strip()   #删除全部空格
print(l)
print(len(l))
print(m)
print(len(m))
print(n)
print(len(n))

# 2.3.5 使用字符串时避免语法错误
print("2.3.5")

message = "One of Python's strengths is its diverse community."
print(message)


print("# ------动手试一试------")

# 2-3：个性化消息
print("2-3")

name = "Eric"
print("Hello",name,",would you like to learn some Python today?")
print("Hello " + name + " ,would you like to learn some Python today?")

# 2-4 调整名字的大小写
print("2-4")

name = "hoNkly"
print(name.lower(),name.upper(),name.title())

# 2-5 名言
print("2-5")
print('Albert Einstein once said,"hello."')

# 2-6 名言2
print("2-6")
famous_person = "honkly"
words = '"I like Python!"'
message = famous_person + " once said, " + words

print(message)

# 2-7 剔除人名中的空白
print("2-7")

name = " \n\thonkly "

print(name)
print(name.rstrip())
print(name.lstrip())
print(name.strip())
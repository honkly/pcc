#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 13:07:45
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 8.1 定义函数
print("8.1")

def greet_user_test():
    """显示简单的问候语"""
    print("Hello!")

greet_user_test()

# 8.1.1 向函数传递信息
print("8.1.1")

def greet_user(username):
    """Display a simple greeting."""
    print("Hello, " + username.title() + "!")
    
greet_user('jesse')

print("------动手试一试------")

# 8-1 消息
print("8-1")

def display_message():
    print("I am learning function!")

display_message()

# 8-2 喜欢的图书
print("8-2")

def favorite_book(title):
    print("My favorite book is 《" + title.title() + "》!")
favorite_book("哈利波特")
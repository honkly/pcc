#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-08 23:44:47
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

import json

filename = 'numbers.json'

def get_new_username():
    number = input("Please input number that your favorite!")
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
    return number   

def greet_user():
    try:
        with open(filename) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        number = get_new_username()
        print("Now I know your favorite number is " + number)
    else:
        print("I know your favorite number!It's " + number)

greet_user()
        
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 16:33:26
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 8.3 返回值
print("8.3")

# 8.3.1 返回简单值
print("8.3.1")

def get_formatted_name_831(first_name, last_name):
    """返回整洁的姓名"""
    full_name = first_name + ' ' + last_name
    return full_name.title()

musician = get_formatted_name_831('jimi', 'hendrix')
print(musician)

# 8.3.2 让实参变成可选的
print("8.3.2")

def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' +  middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
    
musician = get_formatted_name('jimi', 'hendrix')
print(musician)

musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)

# 8.3.3 返回字典
print("8.3.3")

def build_person(first_name, last_name, age=''):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# 8.3.4 结合使用函数和while循环
print("8.3.4")

while True:
    print("Please tell me your name:")
    print("(enter 'q' at any time to quit)")

    first_name = input("First name: ")
    if first_name == 'q':
        break
    last_name = input("Last name: ")
    if last_name == 'q':
        break
    formatted_name = get_formatted_name(first_name, last_name)
    print("\nHello! " + formatted_name + "!")

print("------动手试一试------")

# 8-6 城市名
print("8-6")

def city_country(city, country):
    return city + ',' + country

citys_info = []
for i in range(0,3):
    city_info = city_country('Beijing', 'China')
    citys_info.append(city_info)

for city_info in citys_info:
    print(city_info)

# 8-7 专辑
print("8-7")

def make_album(name, works, Songs_number = ''):
    album = {'name': name, 'works': works}
    if Songs_number:
        album['Songs_number'] = Songs_number

    print(album)

    return album

make_album('lee', 'helloworld')
make_album('honkly', 'hellopython', Songs_number = 12)

# 8-8 用户的专辑
print("8-8")

while True:
    print("Please tell your album:")
    print("(enter 'q' at any time to quit)")

    name = input("Name: ")
    if name == 'q':
        break
    works = input("works: ")
    if works == 'q':
        break
    
    print("Your album is:")
    print(make_album(name, works))
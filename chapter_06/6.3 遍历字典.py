#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 00:34:39
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 6.3.1 遍历所有的键值对
print("6.3.1")

user_0 = {'username': 'efermi',
          'first': 'enrico',
          'last': 'fermi',
          }

for key, value in user_0.items():
    print("\nKey: " + key)
    print("Value: " + value)

favorite_languages = {
    'jen': 'python',
    'honkly': 'python',
    'knight': 'c'
    }

for name,language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# 6.3.2 遍历字典中的所有键
print("6.3.2")

for name in favorite_languages.keys():
    print(name.title())
for name in favorite_languages:
    print(name.title())

favorite_languages = {
    'jen': 'python',
    'honkly': 'python',
    'knight': 'c'
    }

friends = ['phile', 'jen', 'knight']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ",I see your favorite language is " +
            favorite_languages[name].title() + "!")

# 6.3.3 按顺序遍历字典中的所有键
print("6.3.3")

favorite_languages = {
    'jen': 'python',
    'honkly': 'python',
    'knight': 'c',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'c++'
    }

for name in sorted(favorite_languages.keys()):
    print(name)

# 6.3.4 遍历字典中的所有值
print("6.3.4")

print("The following language have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# 集合set
print("# 集合set")
for language in set(favorite_languages.values()):
    print(language)

print("------动手试一试------")

# 6-4 词汇表2
print("6-4")

words = {'print': 'print words', 'input': 'input words'}
for key,value in words.items():
    print(key + ":" + value)

words['while'] = 'while something'
words['if'] = 'if test'

for key,value in words.items():
    print(key + ":\n\t" + value)

# 6-5 河流
print("6-5")

rivers = {'Yangtze': 'china', 'nale': 'egypt', 'yellow': 'china', 'Ganges': 'india'}

for river,country in rivers.items():
    print("The " + river + " runs through " + country)

for river in rivers.keys():
    print(river)

for country in rivers.values():
    print(country)

# 6-6 调查
print("6-6")

favorite_languages = {
    'jen': 'python',
    'honkly': 'python',
    'knight': 'c',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'c++'
    }

current_users = ['honkly', 'phil', 'haha', 'admin', 'root', 'knight']

for name in current_users:
    if name in favorite_languages.keys():
        print("Thanks! " + name)
    else:
        print("Welcome to vote! " + name)
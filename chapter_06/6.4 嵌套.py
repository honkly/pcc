#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 21:26:36
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 6.4 嵌套
print("6.4")

# 6.4.1 字典列表
print("6.4.1")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range (0,30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
    
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15
        
# Show the first 5 aliens:
for alien in aliens[0:5]:
    print(alien)
print("...")

# 6.4.2 在字典中存储列表
print("6.4.2")

# 存储所点比萨的信息
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese']
    }

# 概述所点的比萨
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")

for topping in pizza['toppings']:
    print("\t" + topping)

favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell']
    }

for name,languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite_languages are:")
    for language in languages:
        print("\t" + language.title())

# 6.4.3 在字典中存储字典
print("6.4.3")

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton'
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris'
        },
    }

for username,user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    print("\tFull name: " + full_name.title())
    print("\tLocation: " + user_info['location'].title())

print("------动手试一试------")

# 6-7 人
print("6-7")

friend_1 = {'first_name': 'Knight', 'last_name': 'Lee', 'age': 27, 'city': 'Beijing'}
friend_2 = {'first_name': 'Bernard', 'last_name': 'Lee', 'age': 27, 'city': 'Jinan'} 
friend_3 = {'first_name': 'Kevin', 'last_name': 'Lee', 'age': 24, 'city': 'Qingdao'}

friends = [friend_1, friend_2, friend_3]

for friend in friends:
    full_name = friend['first_name'] + friend['last_name']
    print(full_name.title() + " is " + str(friend['age']) + " years old! " +
        "And now he is in " + friend['city'].title() + "!")

# 6-8 宠物   （待完善）
print("6-8")

robin = {'animal': 'cat', 'master': 'Knight'}
haha = {'animal': 'dog', 'master':'honkly'}

pets = [robin,haha]

for pet in pets:
    print("The " + pet['animal'] + " is belone to " + pet['master'])

# 6-9 喜欢的地方
print("6-9")

favorite_places = {
    'honkly': ['shanghai', 'beijing'],
    'Knight': ['Qingdao', 'Jinan'],
    'Lee': ['shanghai', 'dezhou']
    }

for name,places in favorite_places.items():
    print(name.title() + "'s favorite places is:")
    for place in places:
        print("\t" + place.title())

# 6-10 喜欢的数字
print("6-10")

favorite_number = {
    'honkly': [1,2,3],
    'Knight': [4,5,6],
    'Lee': [7,8,9]
    }
for name,numbers in favorite_number.items():
    print(name.title() + "'s favorite numbers is:")
    for number in numbers:
        print("\t" + str(number))

# 6-11 城市
print("6-11")

cities = {
    'Beijing': {
        'Country': 'China',
        'People': 1300000000,
        'Truth': "Air pollution is serious!"
        },
    'Paris': {
        'Country': 'France',
        'People': 67000000,
        'Truth': "It's a romantic city!"
        }
    }

for city,city_info in cities.items():
    print(city.title() + " is in " + city_info['Country'] +
        ", have " + str(city_info['People']) + " People, " + city_info['Truth']
        )

# 6-12 扩展
print("6-12")

print("略")
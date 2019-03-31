#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 13:30:20
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 8.2.1 位置实参
print("8.2.1")

def describe_pet_821(pet_name, animal_type):
    """Display information about a pet."""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_821('harry', 'hamster')

# 8.2.2 关键字实参
print("8.2.2")

def describe_pet_822(pet_name, animal_type):
    """Display information about a pet."""
    print("I have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet_822(animal_type='hamster', pet_name='harry')
describe_pet_822(pet_name='harry', animal_type='hamster')

# 8.2.3 默认值
print("8.2.3")

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')

# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 8.2.4 等效的函数调用
print("8.2.4")
describe_pet('willie')
describe_pet('harry', 'hamster')

describe_pet(pet_name='willie')
describe_pet('harry', animal_type='hamster')

describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

# 8.2.5 避免实参错误
print("8.2.5")

# describe_pet()

print("------动手试一试------")

# 8-3 T恤
print("8-3")

def make_shirt(size, words):
    print("Size is " + str(size) + ", words are ->" + words)

make_shirt(25, "hello world")

# 8-4 大号T恤
print("8-4")

def make_shirt_84(size, words = "I love Python!"):
    print("Size is " + str(size) + ", words are ->" + words)

make_shirt_84(1)
make_shirt_84(50)
make_shirt_84(99, "I love C++!")

# 8-5 城市
print("8-5")

def describe_city(city_name, city_country = "China"):
    print(city_name.title() + " is in " + city_country + "!")

describe_city("Beijing")
describe_city("Jinan")
describe_city("New York", "American")
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-01 00:03:12
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 9.1.1 创建Dog类
print("9.1.1")

class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age
        
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")
        
# 9.1.2 根据类创建实例
print("9.1.2")

my_dog = Dog('willie', 6)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

# 创建多个实例
your_dog = Dog('lucy', 3)
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()

print("---动手试一试---")
# 9-1 餐馆
print("9-1")

class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def describe_restaurant(self):
        print(self.name + ":" + self.type)

    def open_restaurant(self):
        print("Restaurant is OPEN!")

restaurant = Restaurant('alan','restaurant')
print(restaurant.name,restaurant.type)
restaurant.describe_restaurant()
restaurant.open_restaurant()

# 9-2 三家餐馆
print("9-2")
restaurant_1 = Restaurant('1','1')
restaurant_2 = Restaurant('2','2')
restaurant_3 = Restaurant('3','3')

restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()
restaurant_3.describe_restaurant()

# 9-3 用户
print("9-3")

class User():
    """docstring for User"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print("Hello! " + self.first_name.title() + ' ' + self.last_name.title())

user_1 = User('knight', 'lee')
user_2 = User('kevin', 'lee')

user_1.describe_user()
user_2.greet_user()

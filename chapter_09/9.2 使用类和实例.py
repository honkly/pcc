#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-01 00:03:12
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

class Car():
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        """Initialize attributes to describe a car."""
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = str(self.year) + ' ' + self.manufacturer + ' ' + self.model
        return long_name.title()
    
    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")
        
    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it attempts to roll the odometer back.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

# 9.2.1 Car类
print("9.2.1")

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 9.2.2　给属性指定默认值
print("9.2.2")

# def __init__(self, manufacturer, model, year):
#     """Initialize attributes to describe a car."""
#     self.manufacturer = manufacturer
#     self.model = model
#     self.year = year
#     self.odometer_reading = 0

my_new_car.read_odometer()

# 9.2.3 修改属性的值
print("9.2.3")

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

# 通过方法修改属性的值
my_new_car.update_odometer(30)
my_new_car.read_odometer()

# 通过方法对属性的值进行递增
my_new_car.increment_odometer(100)
my_new_car.read_odometer()

print("------动手试一试------")

# 9-4 就餐人数
print("9-4")

class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type
        self.number_served = 0

    def describe_restaurant(self):
        print(self.name + ":" + self.type)

    def open_restaurant(self):
        print("Restaurant is OPEN!")

    def print_number_served(self):
        print("There are " + str(self.number_served) + " number served")

    def set_number_served(self, number):
    	self.number_served = number

    def increment_number_serverd(self):
        self.number_served += 10
    	
restaurant = Restaurant('ALAN', 'restaurant')
restaurant.print_number_served()
restaurant.number_served = 13
restaurant.print_number_served()

restaurant.set_number_served(666)
restaurant.print_number_served()

restaurant.increment_number_serverd()
restaurant.print_number_served()

# 9-5 尝试登陆次数
print("9-5")

class User():
    """docstring for User"""
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(self.first_name.title() + ' ' + self.last_name.title())

    def greet_user(self):
        print("Hello! " + self.first_name.title() + ' ' + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

    def print_login_attempts(self):
        print("Login attempts are " + str(self.login_attempts))

user_test = User('knight', 'Lee')
user_test.print_login_attempts()
user_test.increment_login_attempts()
user_test.increment_login_attempts()
user_test.print_login_attempts()
user_test.reset_login_attempts()
user_test.print_login_attempts()

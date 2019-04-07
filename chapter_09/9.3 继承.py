#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-04-07 15:40:05
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

"""A set of classes that can be used to represent electric cars."""

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

class Battery():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)
    
        
class ElectricCar(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'Model s', '2016')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("------动手试一试------")

# 9-6 冰淇淋小店
print("9-6")

class Restaurant():
    """docstring for Restaurant"""
    def __init__(self, restaurant_name, restaurant_type):
        self.name = restaurant_name
        self.type = restaurant_type

    def describe_restaurant(self):
        print(self.name + ":" + self.type)

    def open_restaurant(self):
        print("Restaurant is OPEN!")

class IceCreamStand(Restaurant):
    """docstring for IceCreamStand"""
    def __init__(self, restaurant_name, restaurant_type):
        super().__init__(restaurant_name, restaurant_name)
        self.flavors = ['milk', 'apple']

    def print_icecreamstand(self):
        print(self.flavors)

icecreamstand = IceCreamStand('Alan', 'restaurant')
icecreamstand.print_icecreamstand()

# 9-7 管理员
print("9-7")

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

class Amdin(User):
    """docstring for ClassName"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = ['can add post', 'can delete post', 'can ban user']

    def show_privileges(self):
        print(self.privileges)

user_97 = Amdin('Knight', 'lee')
user_97.show_privileges()

# 9-8 权限
print("9-8")

class Privileges():
    def __init__(self):
        self.privileges = ['can add post', 'can delete post', 'can ban user']

class Admin(User):
    """9-8权限"""
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.privileges = Privileges()

user_98 = Admin('Knight', 'Lee')
print(user_98.privileges.privileges)

# 9-9 电瓶升级
print("9-9")

class Battery_99():
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=60):
        """Initialize the batteery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_size) + "-kWh battery.")  
        
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 60:
            range = 140
        elif self.battery_size == 85:
            range = 185
            
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)

    def update_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85
    
        
class ElectricCar_99(Car):
    """Models aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(manufacturer, model, year)
        self.battery = Battery_99()

car_99 = ElectricCar_99('tesla', 'Model s', '2016')
car_99.battery.get_range()
car_99.battery.update_battery()
car_99.battery.get_range()
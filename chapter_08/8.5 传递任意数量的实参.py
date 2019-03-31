#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 21:48:50
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 8.5 传递任意数量的实参
print("8.5")
def make_pizza_85(*toppings):
    """打印顾客点的所有配料"""
    for topping in toppings:
        print(topping)

make_pizza_85('pepperoni')
make_pizza_85('pepperoni', 'mushrooms', 'green peppers', 'extra cheese')

# 8.5.1 结合使用位置实参和任意数量实参
print("8.5.1")

def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)
        
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 8.5.2 使用任意数量的关键字实参
print("8.5.2")

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)

print("------动手试一试------")
#8-12 三明治
print("8-12")

def sandwichs(*toppings):
    print("Your sandwiths:")
    for topping in toppings:
        print("-" + topping)

sandwichs('chiken')
sandwichs('beef', 'chiken', 'milk')

# 8-13 用户简介
print("8-13")

my_profile = build_profile('Knight', 'Lee',
    location='Beijing', 
    field='computer'
    )
print(my_profile)

# 8-14 汽车
print("8-14")

def make_car(manufacturer, model, **car_info):
    """创建cars字典"""
    cars = {}
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    for key,value in car_info.items():
        cars[key] = value
    return cars

car = make_car('subaru','outback',color = 'blue',tow_package=True)
print(car)


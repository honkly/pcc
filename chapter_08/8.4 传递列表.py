#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 17:47:40
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 8.4 传递列表
print("8.4")

def greet_users(names):
    """Print a simple greeting to each user in the list."""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'ty', 'margot']
greet_users(usernames)

# 8.5 在函数中修改列表
print("8.5")

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design, until there are none left.
    Move each design to completed_models after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
    
        # Simulate creating a 3d print from the design.
        print("Printing model: " + current_design)
        completed_models.append(current_design)
        
def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)
        
        
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

print("------动手试一试------")

# 8-9 魔术师
print("8-9")

def show_magicians(magicians):
    for magician in magicians:
        print(magician)

magicians = ['lee', 'honkly', 'knight']
show_magicians(magicians)

# 8-10 了不起的魔术师
print("8-10")
magicians = ['lee', 'honkly', 'knight']
great_magicians = []

def make_great(magicians, great_magicians):
    while magicians:
        magician = magicians.pop()
        great_magician  = 'the great ' + magician
        great_magicians.append(great_magician)

make_great(magicians, great_magicians)
print("Show magicians:")
show_magicians(magicians)
print("Show great magicians:")
show_magicians(great_magicians)

# 8-11 不变的魔术师
print("8-11")
magicians = ['lee', 'honkly', 'knight']
great_magicians = []

make_great(magicians[:], great_magicians)
show_magicians(magicians)
show_magicians(great_magicians)
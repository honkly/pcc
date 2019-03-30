#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-31 00:04:09
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 7.3.1 在列表之间移动元素
print("7.3.1")

# Start out with some users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user, until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print("Verifying user: " + current_user.title())
    confirmed_users.append(current_user)
    
# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

# 7.3.2 删除包含特定值得所有列表元素
print("7.3.2")

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while 'cat' in pets:
    pets.remove('cat')
    
print(pets)

# 7.3.3 使用用户输入俩填充字典
print("7.3.3")

responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")
    
    # Store the response in the dictionary:
    responses[name] = response
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
# Polling is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")

print("------动手试一试------")

# 7-8 熟食店
print("7-8")

sandwich_orders = ['tuna', 'beef', 'chicken']
finished_sandwiches = []

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print("I made your " + current_sandwich + " sandwich!")

    finished_sandwiches.append(current_sandwich)

print(finished_sandwiches)

# 7-9 无香烟熏牛肉(pastrami)卖完了
print("7-9")

sandwich_orders = ['tuna', 'pastrami', 'beef', 'pastrami', 'chicken', 'pastrami']
print(sandwich_orders)
print("pastrami is out of stock!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)

# 7-10 梦想的度假胜地
print("7-10")

places = {}

while True:
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world,where woule you go? ")
    places[name] = place
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        break

for name, place in places.items():
    print(name.title() + " would like to climb " + place.title() + ".")
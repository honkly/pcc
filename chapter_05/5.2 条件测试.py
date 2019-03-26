#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-27 00:05:09
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 5.2 条件测试
print("5.2")

# 5.2.1 检查是否相等
print("5.2.1")

car = 'bmw'
print(car == 'bmw')

# 5.2.2 检查是否相等时不考虑大小写
print("5.2.2")

car = 'Audi'
print(car == 'audi')
print(car.lower() == 'audi')

# 5.2.3 检查是否不相等
print("5.2.3")

requested_topping = 'mushrooms'

if requested_topping != 'anchovies':
    print("Hold the anchovies!")

# 5.2.4 比较数字
print("5.2.4")

age = 18
print(age ==18)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")

# 小于等于
print(age <= 20)
# 小于
print(age < 20)
# 大于
print(age > 20)
# 大于等于
print(age >= 20)

# 5.2.5 检查多个条件
print("5.2.5")

# 1.and
age_0 = 22
age_1 = 18
print(age_0 >= 21 and age_1 >=21)
age_1 = 22
print(age_0 >= 21 and age_1 >=21)

# 2.or
age_0 = 22
age_1 = 18
print(age_0 >= 21 or age_1 >=21)
age_0 = 18
print(age_0 >= 21 or age_1 >=21)

# 5.2.6 检查特定值是否包含在列表中
print("5.2.6")

number_list = ['1', '2', '3']
print('3' in number_list)

# 5.2.7 检查特定值是否不包含在列表中
print("5.2.7")

print('5' not in number_list)

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:
    print(user.title() + ", you can post a response if you wish.")

print("------动手试一试------")

# 5-1 条件测试
print("5-1")

car = 'Audi'

print("Is car == 'subaru'? I predict False.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict True")
print(car.lower() == 'audi')

# 5-2 更多的条件测试
print("5-2")

# 检查2个字符串相等和不等
print("# 检查2个字符串相等和不等")

print('ab' == 'ab')
print('ab' != 'ab')

# 使用函数lower()的测试
print("# 使用函数lower()的测试")

print('Ab'.lower() == 'ab')
print('Ab'.lower() == 'ab')

# 检查2个数字相等、不等、大于、小于、、大于等于、小于等于
print("# 检查2个数字相等、不等、大于、小于、、大于等于、小于等于")

print(2 == 3, 2 !=3 ,2 > 3, 2 < 3, 2 >= 3, 2 <= 3)

# 使用关键字and和or的测试
print("# 使用关键字and和or的测试")

print(2 < 3 and 3 < 4)
print(2 < 3 and 3 > 4)
print(2 < 3 or 3 > 4)

# 测试特定的之是否包含在列表中
print("# 测试特定的之是否包含在列表中")

number_list = [1,2,3]
print(1 in number_list)

# 测试特定的之是否未包含在列表中
print("# 测试特定的之是否未包含在列表中")

print(5 not in number_list)

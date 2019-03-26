#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-25 23:56:27
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 4.3 创建数值列表

# 4.3.1 使用函数range()
print("4.3.1")

for value in range(1,5):
	print(value)

# 4.3.2 使用range()创建数字列表
print("4.3.2")

numbers = list(range(1,6)) 
print(numbers) 

# 指定步长
even_numbers = list(range(2,11,2)) 
print(even_numbers)

# 平方值加入到列表中
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)
	# squares.append(value**2)

print(squares)

# 4.3.3 对数字列表执行简单的统计计算
print("4.3.3")
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# 4.3.4 列表解析
print("4.3.4")

squares = [value**2 for value in range(1,11)]
print(squares)

print("------动手试一试------")

# 4-3 数到20
print("4-3")
for value in range(1,21):
	print(value)

# 4-4 一百万
print("4-4")

number_list = list(range(1,101))
print(number_list)

# 4-5 计算1~100的总和
print(max(number_list))
print(min(number_list))
print(sum(number_list))

# 4-6 奇数
print("4-6")
odd_number =  [value for value in range(1,20,2)]
print(odd_number)

# 4-7 3的倍数
print("4-7")

number_list = []
for value in range(3,30):
	if value%3 == 0:
		number_list.append(value)

print(number_list)

# 4-8 立方
print("4-8")
number_list = []
for value in range(1,11):
	number_list.append(value**3)
print(number_list)

# 4-9 立方解析
print("4-9")
number_list = [value**3 for value in range(1,11)]
print(number_list)

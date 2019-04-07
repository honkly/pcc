#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 00:34:39
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 9-14 骰子
print("9-14")

from random import randint

class Dice():
    def __init__(self, sides=6):
        self.sides = sides
        self.number = 0

    def roll_dice(self):
        self.number = randint(1, self.sides)

    def describe_dice(self):
        print(self.number)
print("6面的骰子10次：")
my_dice = Dice()
for i in range(0, 10):
    my_dice.roll_dice()
    my_dice.describe_dice()

# 创建一个10面的骰子，投掷10次
print("10面的骰子10次：")
my_dice_10 = Dice(10)
for i in range(0, 10):
    my_dice_10.roll_dice()
    my_dice_10.describe_dice()

# 创建一个20面的骰子，投掷10次
print("20面的骰子10次：")
my_dice_20 = Dice(20)
for i in range(0, 10):
    my_dice_20.roll_dice()
    my_dice_20.describe_dice()





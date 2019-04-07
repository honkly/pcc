#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-03-28 00:34:39
# @Author  : Yong Lee (honkly@163.com)
# @Link    : http://www.cnblogs.com/honkly/
# @Version : 1.0

# 9-13 使用OrderedDict
print("9-13")

from collections import OrderedDict

words = OrderedDict()

words['print'] = 'print words'
words['input'] = 'input words'
words['while'] = 'while something'
words['if'] = 'if test'

for key,value in words.items():
    print(key + ":\n\t" + value)
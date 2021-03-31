# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:function.py
@time:2021/03/30
"""
import random


def bin_weight_random(out1, out2, weight):  # 二元权重随机
    r = random.random()
    if r < weight:
        return out1
    else:
        return out2


def gen_names(list1, list2, list3, list4):
    l = len(list1) - 1
    num1 = 0
    num2 = 0
    while num1 == num2:
        num1 = random.randint(0, l)
        num2 = random.randint(0, l)
    name_en = list3[num1] + '·' + list1[num2]
    name_zh = list4[num1] + '·' + list2[num2]
    name = [name_en, name_zh]
    return name


def gen_birth():
    year = random.randint(1960, 1999)
    month = random.randint(1, 12)
    day = random.randint(1, 29)
    return [year, month, day]


def gen_gen():
    m = '男'
    f = '女'
    gen = bin_weight_random(m, f, 0.8)
    return gen

# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:reData.py
@time:2021/03/30
"""
import csv

with open('data/names.txt', encoding='utf-8') as n:
    c = open('data/csv/familyNames.csv', 'w', newline='')
    c_w = csv.writer(c)
    for name in n.readlines():
        name = name.split(' ')
        print(name)
        c_w.writerow(name[0:2])

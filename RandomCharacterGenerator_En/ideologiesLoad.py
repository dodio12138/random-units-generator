# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:ideologiesLoad.py
@time:2021/03/31
"""

import json

with open('data/csv/ideologies_copy.json', 'r', encoding='utf-8') as ide:
    data = [{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
    data_ide = json.load(ide)
    cor = 0
    test = [5, 3, 6, 7]
    for i in range(len(data_ide['ideologies'])):
        stats = data_ide['ideologies'][i]['stats']
        
        print(stats)

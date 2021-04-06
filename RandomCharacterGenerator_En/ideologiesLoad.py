# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:ideologiesLoad.py
@time:2021/03/31
"""

import json
import math
import matplotlib.pyplot as plt
import time
import random
import csv
import numpy as np


def EuclideanMetric(x, y):  # 计算欧式距离
    e = math.sqrt(
        math.pow(x[0] - y[0], 2) + math.pow(x[1] - y[1], 2) + math.pow(x[2] - y[2], 2) + math.pow(x[3] - y[3], 2))
    return e


def pic(c):
    plt.figure(dpi=100)
    x = list(range(52))
    plt.xticks(range(0, 51, 1), fontsize=5)
    plt.plot(x, c, 'b')
    plt.plot(x, c, 'or', ms=2)
    plt.show()


def out_ideCode(stats):  # 意识形态标识码
    ideCode = [0, 0, 0, 0]
    for i in range(4):
        if stats[i] >= 8:
            ideCode[i] = -2
        elif stats[i] >= 6:
            ideCode[i] = -1
        elif stats[i] == 5:
            ideCode[i] = 0
        elif stats[i] >= 3:
            ideCode[i] = 1
        else:
            ideCode[i] = 2
    return ideCode


def gen_ide(seed, wieght):  # 生成特定随机意识形态
    stats = [0, 0, 0, 0]
    for i in range(4):
        if seed[i] == -1:
            stats[i] = np.random.randint(0, 10)
        else:
            stats[i] = np.random.randint(seed[i] - wieght, seed[i] + wieght)
    for j in range(4):  # 限制大小
        if stats[j] > 10:
            stats[j] = 10
        elif stats[j] < 0:
            stats = 0
        else:
            pass
    return stats


start = time.process_time()
with open('data/csv/ideologies_copy.json', 'r', encoding='utf-8') as ide:  # 打开json数据
    # t = open('data/csv/ideIndex.csv', 'w', encoding='utf-8-sig', newline='')  # 打开csv数据
    data = [{"a": 1, "c": 3, "b": 2, "e": 5, "d": 4}]
    data_ide = json.load(ide)  # 载入json文件
    cor = []  # 相似度序列
    stats = [0, 0, 0, 0]  # 意识形态统计
    times = 10
    while times > 0:
        test = gen_ide([8, -1, 3, -1], wieght=1)
        for i in range(len(data_ide['ideologies'])):
            stats[0] = data_ide['ideologies'][i]['stats']['econ']
            stats[1] = data_ide['ideologies'][i]['stats']['dipl']
            stats[2] = data_ide['ideologies'][i]['stats']['govt']
            stats[3] = data_ide['ideologies'][i]['stats']['scty']
            cor.append(EuclideanMetric(test, stats))
            # csv_ide = csv.writer(t)  # 载入csv
            # csv_ide.writerow([str(i), str(data_ide['ideologies'][i]['name_zh']), str(out_ideCode(stats))])  # 写入csv信息
        times -= 1
        index = cor.index(min(cor))
        rep = cor.count(min(cor))
        print(data_ide['ideologies'][index], '\n', test)
        # print(rep)
        # if rep == 2:
        #     pic(cor)
        #     print(data_ide['ideologies'][index], test)
        cor.clear()
    end = time.process_time()
    print(end - start)

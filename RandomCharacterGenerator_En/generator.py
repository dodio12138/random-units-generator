# -*- coding: UTF-8 -*-
"""
@author:dodio
@description:
@file:generator.py
@time:2021/03/30
"""
import time
from scripts import function as f

if __name__ == '__main__':
    # 从csv中提取姓名群组
    familyNames_en = []
    familyNames_zh = []
    faN = open('data/csv/familyNames.csv', 'r')
    out = open('data/100units.txt', 'w')
    j = 0
    for i in faN.readlines():
        i = i.strip('\n').split(',')
        familyNames_en.append(i[0])
        familyNames_zh.append(i[1])
        j += 1
    fristNames_en = familyNames_en.copy()
    fristNames_zh = familyNames_zh.copy()

    person = []
    frequency = 1
    femaleNum = 0
    while frequency > 0:
        person = f.gen_names(familyNames_en, familyNames_zh, fristNames_en, fristNames_zh)
        person.append(f.gen_gen())
        person.append(f.gen_birth())
        # time.sleep(0.1)
        # print(person)
        l_data = '姓名：' + str(person[1]) + '(' + str(person[0]) + ')    ' + '性别：' + str(
            person[2]) + '    ' + '出生日期：' + str(
            person[3][0]) + '.' + str(
            person[3][1]) + '.' + str(person[3][2])
        out.write(l_data)
        out.write('\n')
        if str(person[2]) == '女':
            femaleNum += 1
        print(femaleNum)
        frequency -= 1

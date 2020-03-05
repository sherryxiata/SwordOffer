#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 14:33
# @Author  : wenlei

#变态青蛙跳

'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

def jumpFloorII(number):
    # write code here
    if number < 0:
        return 0
    res = [0, 1]
    while len(res) <= number:
        res.append(sum(res) + 1)
    return res[number]

if __name__ == '__main__':
    print(jumpFloorII(-1))
    print(jumpFloorII(0))
    print(jumpFloorII(1))
    print(jumpFloorII(2))
    print(jumpFloorII(3))
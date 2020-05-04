#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 14:20
# @Author  : wenlei

'''青蛙跳台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法（先后次序不同算不同的结果）。
'''

#找规律：发现是斐波那契数列； n=5：从第4级上来/从第3级上来

def jumpFloor(number):
    # write code here
    if number <0:
        return 0
    res = [0,1,2]
    while len(res) <= number:
        res.append(res[-1]+res[-2])
    return res[number]

if __name__ == '__main__':
    print(jumpFloor(-1))
    print(jumpFloor(0))
    print(jumpFloor(1))
    print(jumpFloor(2))
    print(jumpFloor(3))
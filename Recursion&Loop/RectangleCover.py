#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 15:28
# @Author  : wenlei

'''矩形覆盖问题

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？
'''

#第一块矩形横着放：f(n-2) 第一块矩形竖着放：f(n-1)

def rectCover(number):
    # write code here
    if number < 0:
        return 0
    res = [0, 1, 2]
    while len(res) <= number:
        res.append(res[-1] + res[-2])
    return res[number]

if __name__ == '__main__':
    print(rectCover(-1))
    print(rectCover(0))
    print(rectCover(1))
    print(rectCover(2))
    print(rectCover(3))
    print(rectCover(4))

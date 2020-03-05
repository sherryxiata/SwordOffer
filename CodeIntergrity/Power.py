#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/5 20:26
# @Author  : wenlei

# 数值的整数次方

'''
给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。
保证base和exponent不同时为0
'''

# #简单解法
# def Power(base, exponent):
#     # write code here
#     if exponent == 0:
#         return 1
#     temp = 1
#     if exponent > 0:
#         for i in range(exponent):
#             temp = temp * base
#         return temp
#     else:
#         for i in range(-exponent):
#             temp = temp * base
#         return 1 / temp

#快速幂解法；快速幂：https://blog.csdn.net/hkdgjqr/article/details/5381028
def Power(base,exponent):
    if exponent == 0:
        return 1
    tmp = base
    res = 1
    e = abs(exponent)
    while(e>0):
        if e&1 : #说明该位置是1，需要加入连乘
           res = res * tmp
        e = e >> 1 #a>>1=a/2
        tmp = tmp * tmp #继续按连乘增长
    return res if exponent > 0 else 1/res

if __name__ == '__main__':
    print(Power(0,6)) #0
    print(Power(6.6,0)) #1
    print(Power(2,3)) #8
    print(Power(-2,3)) #-8
    print(Power(2,-3)) #0.125
    print(Power(-2,-3)) #-0.125
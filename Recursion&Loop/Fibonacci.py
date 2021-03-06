#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/3/4 13:50
# @Author  : wenlei

'''斐波那契数列

大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。n<=39
'''


def Fibonacci(n):
    res = [0,1]
    while len(res) <= n:
        res.append(res[-2] + res[-1])
    return res[n]

#由于第n项的值只与前两项有关，所以只需保留前两项，将空间复杂度从O(N)降到O(1)
def Fibonacci(n):
    if n <= 1:
        return n
    pre2 = 0
    pre1 = 1
    for i in range(n-1):
        fib =  pre2 + pre1
        pre2 = pre1
        pre1 = fib
    return fib

if __name__ == '__main__':
    print(Fibonacci(0))
    print(Fibonacci(1))
    print(Fibonacci(2))
    print(Fibonacci(5))
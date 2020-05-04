#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/4 16:20
# @Author  : wenlei

'''
二进制中1的个数

输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。
'''

class Solution:
    def NumberOf1(self, n):
        # write code here
        #计算二进制表示
        bi = bin(n)
        if n > 0:
            s = str(bi[2:])
        print(s)
        count = s.count(1)
        return count

if __name__ == '__main__':
    X = Solution()
    print(X.NumberOf1(11))

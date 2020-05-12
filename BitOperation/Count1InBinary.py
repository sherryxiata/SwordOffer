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

        #解法1
        #return bin(n).replace('0b','').count('1') if n >= 0 else bin(n + 2**32).replace('0b','').count('1')
        count = 0

        #解法2
        if n < 0:
            n = n & 0xffffffff
        '''
        解释：负数在计算机中以补码形式保存，bin()返回的是二进制。
        由于python的负数理论上为无限位数，而不像c++超过32位就会溢出，所以需要与一个32位全为1的数（0xffffffff）进行与运算，
        相当于将1111(n位)...101111101(32位)变为0000(n位)...101111101(32位)，避免负数1的无限循环。
        '''
        while n:
            count += 1
            n &= n-1 #此位运算可将最后一位的1变为0
        return count

if __name__ == '__main__':
    X = Solution()
    print(X.NumberOf1(11))
    print(X.NumberOf1(0))

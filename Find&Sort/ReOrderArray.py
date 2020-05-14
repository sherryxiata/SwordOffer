#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 11:24
# @Author  : wenlei

'''调整数组顺序使奇数位于偶数前面

输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后半部分，
并保证奇数和奇数，偶数和偶数之间的相对位置不变。
'''

#解法1：设置两个辅助数组，时间：O(N) 空间：O(N)
class Solution:
    def reOrderArray(self, array):
        # write code here
        odd = []
        even = []
        for i in range(len(array)):
            if array[i] % 2 != 0:
                odd.append(array[i])
            else:
                even.append(array[i])
        return odd + even

#设置一个辅助数组
class Solution:
    def reOrderArray(self, array):
        # write code here
        oddCnt = 0 #奇数个数
        for i in range(len(array)):
            if array[i] % 2 != 0:
                oddCnt += 1

        res = [0] * len(array)
        oddInd = 0
        evenInd = oddCnt

        for j in range(len(array)):
            if array[j] % 2 != 0:
                res[oddInd] = array[j]
                oddInd += 1
            else:
                res[evenInd] = array[j]
                evenInd += 1
        return res

#解法2：冒泡法，每次将最后一个偶数移到数组最后 时间；O(N^2) 空间：O(1)
class Solution:
    def reOrderArray(self, array):
        for i in range(len(array) - 1,0,-1):
            for j in range(0,i):
                if array[j] % 2 == 0 and array[j + 1] % 2 != 0:
                    #交换
                    tmp = array[j + 1]
                    array[j + 1] = array[j]
                    array[j] = tmp
        return array

if __name__ == '__main__':
    X = Solution()
    print(X.reOrderArray([1,4,5,2,6,8]))

#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 17:01
# @Author  : wenlei

#旋转数组的最小数字

'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。
输入一个非递减排序的数组的一个旋转，输出旋转数组的最小元素。
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

#非递减排序：不是单调递增，可能存在重复数字

def minNumberInRotateArray(rotateArray):
    # write code here
    if not rotateArray:
        return 0
    for i in range(len(rotateArray) - 1):
        if rotateArray[i] > rotateArray[i + 1]:
            return rotateArray[i + 1]

if __name__ == '__main__':
    # arr = [4,5,6,7,1,2,3]
    # arr = [4,5,5,6,7,7,1,1,2,3]
    arr = [1,3,1]
    res = minNumberInRotateArray(arr)
    print(res)
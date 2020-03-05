#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/11/27 20:41
# @Author  : wenlei

#数组：二维数组中的查找

'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

# -*- coding:utf-8 -*-
# 解法1：直接遍历
#时间复杂度：O（n^2) 空间复杂度：O（1）
class Solution:
    # Array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[i])):
                if(array[i][j] == target):
                    return True
        return False

#解法2：从左下开始找：对于左下角值m，m是该行最小值+该列最大值，
#if m<traget: 剔除这一行
#if m>target: 剔除这一列
#时间复杂度：O（行数+列数） 空间复杂度：O（1）
class Solution:
    # Array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0])

        row = rows-1
        col = 0

        while(row > -1 and col < cols):
            if (array[row][col] < target):
                col += 1
            elif (array[row][col] > target):
                row -= 1
            else:
                return True

        return False

# 解法3：遍历每行，二分查找
#时间复杂度：O（n*logn) 空间复杂度：O（1）
class Solution:
    # Array 二维列表
    def Find(self, target, array):
        # write code here
        rows = len(array)
        cols = len(array[0])

        for i in range(rows):
            low = 0
            high = cols-1

            while(low <= high):
                mid = int((low + high) / 2)
                print(array[i][mid])
                if (target > array[i][mid]):
                    low = mid+1
                elif (target < array[i][mid]):
                    high = mid-1
                else:
                    return True

        return False



#输入array是list,不是np.Array，所以没有shape属性
#array的维度如何获取?
#二分查找


if __name__ == '__main__':
    arr = Solution()
    print(arr.Find(1,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
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
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        for i in range(len(array)):
            for j in range(len(array[i])):
                if(array[i][j] == target):
                    return True
        return False

#输入array是list,不是np.array，所以没有shape属性
#array的维度如何获取


if __name__ == '__main__':
    arr = Solution()
    print(arr.Find(7,[[1,2,8,9],[2,4,9,12],[4,7,10,13],[6,8,11,15]]))
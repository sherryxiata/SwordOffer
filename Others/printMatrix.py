#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 9:59
# @Author  : wenlei

'''顺时针打印矩阵

输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字，
例如，如果输入如下4 X 4矩阵：
 1 2 3 4
 5 6 7 8
 9 10 11 12
 13 14 15 16
 则依次打印出数字1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10.
'''

#解法1
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        res = []
        r1 = 0
        r2 = len(matrix) - 1
        c1 = 0
        c2 = len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for i in range(c1, c2 + 1):
                res.append(matrix[r1][i])
            for i in range(r1 + 1, r2 + 1):
                res.append(matrix[i][c2])
            if r1 != r2:
                for i in range(c2 - 1, c1 - 1, -1):
                    res.append(matrix[r2][i])
            if c1 != c2:
                for i in range(r2 - 1, r1, -1):
                    res.append(matrix[i][c1])
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1
        return res

#解法2：旋转魔法，一直输出第一行
    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            #逆时针旋转矩阵
            matrix = list(map(list, zip(*matrix)))[::-1] #解压操作 + 倒序输出
        return res

if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
    X = Solution()
    print(X.printMatrix(matrix))
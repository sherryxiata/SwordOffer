#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 14:37
# @Author  : wenlei

'''栈的压入、弹出序列

输入两个整数序列，第一个序列表示栈的压入顺序，请判断第二个序列是否可能为该栈的弹出顺序。假设压入栈的所有数字均不相等。
例如序列1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1是该压栈序列对应的一个弹出序列，但4,3,5,1,2就不可能是该压栈序列的弹出序列。
（注意：这两个序列的长度是相等的）

'''
class Solution:
    #使用一个栈来模拟压入弹出操作
    def IsPopOrder(self, pushV, popV):
        # write code here
        if not pushV or not popV:
            return False
        stack = []
        j = 0
        for i in range(0,len(pushV)):
            stack.append(pushV[i])
            while stack and stack[-1] == popV[j]:
                stack.pop()
                j += 1
        if not stack:
            return True
        else:
            return False


if __name__ == '__main__':
    pushV = [1,2,3,4,5]
    popV1 = [4,5,3,2,1]
    popV2 = [4,3,5,1,2]
    X = Solution()
    print(X.IsPopOrder(pushV,popV1))
    print(X.IsPopOrder(pushV,popV2))




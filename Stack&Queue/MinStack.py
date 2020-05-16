#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 11:12
# @Author  : wenlei

'''包含min函数的栈

定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。
'''

class Solution:
    def __init__(self):
        self.stack = []
        self.minList = []

    def push(self, node):
        # write code here
        if not self.minList:
            self.minList.append(node)
        else:
            self.minList.append(min(self.minList[-1],node))
        self.stack.append(node)

    #弹出栈顶元素
    def pop(self):
        # write code here
        if not self.stack:
            return None
        self.minList.pop()
        return self.stack.pop()

    #获得栈顶元素，不弹出
    def top(self):
        # write code here
        if not self.stack:
            return None
        return self.stack[-1]

    def min(self):
        # write code here
        if not self.minList:
            return None
        return self.minList[-1]

if __name__ == '__main__':
    X = Solution()

    X.push(1)
    X.push(2)
    X.push(3)
    X.push(4)
    X.push(5)

    print(X.pop())
    print(X.pop())
    print(X.pop())

    print(X.top())

    print(X.min())
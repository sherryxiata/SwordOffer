#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 19:39
# @Author  : wenlei

'''用两个栈实现队列

用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

###思路：
#当插入时，直接插入 stack1。
#当弹出时，先将stack1的元素push入stack2，再pop stack2
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, node):
        # write code here
        self.stack1.append(node)

    def pop(self):
        # return xx
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            return None
        return self.stack2.pop()

if __name__ == '__main__':
    test = Solution()

    test.push(1)
    print(test.pop())
    print(test.pop())

    # test.push(1)
    # test.push(2)
    # test.push(3)
    # test.push(4)
    # test.push(5)
    #
    # print(test.pop())
    # print(test.pop())
    # print(test.pop())
    # print(test.pop())
    # print(test.pop())



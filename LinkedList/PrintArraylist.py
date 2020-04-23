#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 18:23
# @Author  : wenlei

'''链表：从尾到头打印链表

输入一个链表，按链表从尾到头的顺序返回一个ArrayList。
'''

class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
       if listNode == None:
           return []
       return self.printListFromTailToHead(listNode.next) + [listNode.val]

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    X = Solution()
    result = X.printListFromTailToHead(a)
    print(result)
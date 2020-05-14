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

#解法1：递归
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
       if listNode == None:
           return []
       return self.printListFromTailToHead(listNode.next) + [listNode.val]

#解法2：使用头插法重建逆序链表
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []

        head = ListNode(-1) #辅助头节点，方便插入
        while listNode != None:
            memo = listNode.next
            listNode.next = head.next
            head.next = listNode
            listNode = memo

        res = []
        head = head.next
        while head != None:
            res.append(head.val)
            head = head.next
        return res

#解法3：在遍历链表时将值放入栈，再pop即为逆序。但是python没有栈

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    X = Solution()
    result = X.printListFromTailToHead(a)
    print(result)
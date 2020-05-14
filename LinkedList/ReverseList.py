#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 17:07
# @Author  : wenlei

'''反转链表

输入一个链表，反转链表后，输出新链表的表头。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode

#解法1：递归
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        next = pHead.next
        pHead.next = None
        newHead = self.ReverseList(next)
        next.next = pHead
        return newHead

#解法2：头插法
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        head = ListNode(-1)
        while pHead:
            memo = pHead.next
            pHead.next = head.next
            head.next = pHead
            pHead = memo

        return head.next

if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    X = Solution()
    result = X.ReverseList(a)
    print(result)
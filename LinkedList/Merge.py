#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 19:35
# @Author  : wenlei

'''合并两个排序的链表

输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 返回合并后列表
    # 解法1：外排法
    def Merge(self, pHead1, pHead2):
        # write code here
        head = ListNode(-1)
        cur = head
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                cur.next = pHead1
                pHead1 = pHead1.next
            else:
                cur.next = pHead2
                pHead2 = pHead2.next
            cur = cur.next
        if pHead1:
            cur.next = pHead1
        if pHead2:
            cur.next = pHead2
        return head.next

# 解法2：递归
    def Merge(self, pHead1, pHead2):
        # write code here
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val <= pHead2.val:
            pHead1.next = self.Merge(pHead1.next,pHead2)
            return pHead1
        else:
            pHead2.next = self.Merge(pHead1, pHead2.next)
            return pHead2


if __name__ == '__main__':
    pHead1 = ListNode(1)
    b1 = ListNode(3)
    c1 = ListNode(5)
    pHead1.next = b1
    b1.next = c1

    pHead2 = ListNode(2)
    b2 = ListNode(4)
    c2 = ListNode(6)
    pHead2.next = b2
    b2.next = c2

    X = Solution()
    arr = []
    result = X.Merge(pHead1,pHead2)
    while result:
        arr.append(result.val)
        result = result.next
    print(arr)

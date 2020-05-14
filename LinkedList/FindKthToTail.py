#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 16:27
# @Author  : wenlei

'''链表中倒数第k个结点

输入一个链表，输出该链表中倒数第k个结点。
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def len(self,head):
        len = 1
        while head.next:
            len += 1
            head = head.next
        return len

# 解法1：计算链表长度len，则倒数第k个节点=正数第len-k+1个节点
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        len = self.len(head)
        if k <= 0 or k > len:
            return None
        for i in range(len - k):
            head = head.next
        #注意：题目要求返回节点而不是节点值
        return head

#解法2：设置两个指针p1和p2，p1先动k个节点，p1和p2一起移动，当p1移动到链表尾部时，p2所指的就是倒数第k个节点
    def FindKthToTail(self, head, k):
        # write code here
        if not head:
            return None
        p1 = head
        p2 = head
        while p1 and k > 0:
            p1 = p1.next
            k -= 1
        if k > 0:
            return None
        while p1:
            p1 = p1.next
            p2 = p2.next
        return p2


if __name__ == '__main__':
    a = ListNode(3)
    b = ListNode(4)
    c = ListNode(5)
    a.next = b
    b.next = c

    X = Solution()
    result = X.FindKthToTail(a,2)
    print(result)
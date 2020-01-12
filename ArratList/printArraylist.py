# -*- coding: utf-8 -*-
# @Time    : 2019/12/1 18:23
# @Author  : wenlei

#链表：从尾到头打印链表

'''
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
        arr = []
        while listNode.next != None:
            arr.append(listNode.val)
            next = listNode.next
        return arr

if __name__ == '__main__':
    a_lst = ListNode(3)
    print(lst.next)
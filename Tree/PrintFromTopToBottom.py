#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/16 12:13
# @Author  : wenlei

'''从上往下打印出二叉树

从上往下打印出二叉树的每个节点，同层节点从左至右打印。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    #解法1
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        res = []
        layer = [root]
        while layer:
            this_res = []
            next_layer = []
            for node in layer:
                this_res.append(node.val)
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            layer = next_layer
            res += this_res
        return res

#解法2：用队列实现

if __name__ == '__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    a.left = b
    a.right = c
    b.left = d
    c.left = e
    c.right = f

    X = Solution()
    print(X.PrintFromTopToBottom(a))

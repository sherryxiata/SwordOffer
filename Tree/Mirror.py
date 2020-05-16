#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/15 10:06
# @Author  : wenlei

'''二叉树的镜像

操作给定的二叉树，将其变换为源二叉树的镜像。
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if not root:
            return
        self.swap(root)
        self.Mirror(root.left)
        self.Mirror(root.right)

    def swap(self,root):
        tmp = root.left
        root.left = root.right
        root.right = tmp

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
    X.Mirror(a)
    print(a.left.val)

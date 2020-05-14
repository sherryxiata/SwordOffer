#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/5/14 20:19
# @Author  : wenlei

'''树的子结构

输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
输入格式：{8,8,7,9,2,#,#,#,#,4,7},{8,9,2}
'''


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if not pRoot1 or not pRoot2:
            return False
        return self.isSubTreeWithRoot(pRoot1,pRoot2) or self.HasSubtree(pRoot1.left,pRoot2) or self.HasSubtree(pRoot1.right,pRoot2)

    def isSubTreeWithRoot(self,root1,root2):
        if not root2:
            return True
        if not root1:
            return False
        if root1.val != root2.val:
            return False
        return self.isSubTreeWithRoot(root1.left,root2.left) and self.isSubTreeWithRoot(root1.right,root2.right)


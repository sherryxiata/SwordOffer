#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 17:31
# @Author  : wenlei

#树：重建二叉树

'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if not pre or not tin: #判断list、tuple、dict是否为空
            return None
        root = TreeNode(pre.pop(0)) #pop(key):删除字典给定键 key 及对应的值，返回值为被删除的值。
        index = tin.index(root.val) #index(Str):返回str所处的index
        root.left = self.reConstructBinaryTree(pre, tin[:index])
        root.right = self.reConstructBinaryTree(pre, tin[index + 1:])
        return root

#前序遍历二叉树
def preTraversal(TreeNode):
    if TreeNode == None:
        return []
    return [TreeNode.val] + preTraversal(TreeNode.left) + preTraversal(TreeNode.right)

#中序遍历二叉树
def tinTraversal(TreeNode):
    if TreeNode == None:
        return []
    return tinTraversal(TreeNode.left) + [TreeNode.val] + tinTraversal(TreeNode.right)

#后序遍历二叉树
def postTraversal(TreeNode):
    if TreeNode == None:
        return []
    return postTraversal(TreeNode.left) + postTraversal(TreeNode.right) + [TreeNode.val]


if __name__ == '__main__':
    bTree = Solution()
    # pre = {0:1,1:2,3:4,4:7,5:3,6:5,7:6,8:8}
    # tin = {0:4,1:7,2:2,3:1,4:5,5:3,6:8,7:6}
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    tree = bTree.reConstructBinaryTree(pre,tin)
    print(preTraversal(tree))
    print(tinTraversal(tree))
    print(postTraversal(tree))




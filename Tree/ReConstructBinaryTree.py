#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 17:31
# @Author  : wenlei

'''树：重建二叉树

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
        root = TreeNode(pre.pop(0)) #pop(key):返回并删除list的第一个元素
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

#层次遍历
def level_order(root):
    if root == None:
        return []
    layer = [root]
    res = []
    while layer:
        this_res = [] #这一层的遍历结果
        next_l = [] #下一层的根节点
        for i in layer:
            this_res.append(i.val)
            if i.left:
                next_l.append(i.left)
            if i.right:
                next_l.append(i.right)
        res.append(this_res)
        layer = next_l
    return res

if __name__ == '__main__':
    X = Solution()
    pre = [1,2,4,7,3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    tree = X.reConstructBinaryTree(pre,tin)
    print(preTraversal(tree))
    print(tinTraversal(tree))
    print(postTraversal(tree))
    print(level_order(tree))




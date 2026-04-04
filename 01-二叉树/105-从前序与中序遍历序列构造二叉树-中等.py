"""
105. 从前序与中序遍历序列构造二叉树
https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

给定两个整数数组 preorder 和 inorder ，其中 preorder 是二叉树的先序遍历， inorder 是同一棵树的中序遍历，请构造二叉树并返回其根节点。

示例 1：
输入: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
输出: [3,9,20,null,null,15,7]

示例 2：
输入: preorder = [-1], inorder = [-1]
输出: [-1]
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        递归解法：
        - 前序遍历的第一个元素是根节点
        - 在中序遍历中找到根节点位置，左边是左子树，右边是右子树
        - 递归构建左右子树
        时间复杂度：O(n)
        空间复杂度：O(n)，用于存储中序索引映射
        """
        # 构建中序遍历的值到索引的映射
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        def build(pre_left: int, pre_right: int, in_left: int, in_right: int) -> Optional[TreeNode]:
            if pre_left > pre_right:
                return None
            
            # 前序遍历的第一个元素是根节点
            root_val = preorder[pre_left]
            root = TreeNode(root_val)
            
            # 在中序遍历中找到根节点的位置
            in_root_idx = inorder_map[root_val]
            
            # 左子树的节点数
            left_tree_size = in_root_idx - in_left
            
            # 递归构建左子树
            root.left = build(pre_left + 1, pre_left + left_tree_size, 
                             in_left, in_root_idx - 1)
            
            # 递归构建右子树
            root.right = build(pre_left + left_tree_size + 1, pre_right,
                              in_root_idx + 1, in_right)
            
            return root
        
        return build(0, len(preorder) - 1, 0, len(inorder) - 1)

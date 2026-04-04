"""
230. 二叉搜索树中第K小的元素
https://leetcode.cn/problems/kth-smallest-element-in-a-bst/description/

给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。

示例 1：
输入：root = [3,1,4,null,2], k = 1
输出：1

示例 2：
输入：root = [5,3,6,2,4,null,null,1], k = 3
输出：3
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        中序遍历解法：
        - 二叉搜索树的中序遍历是有序的
        - 找到第k个访问的节点即可
        时间复杂度：O(H + k)，H为树的高度
        空间复杂度：O(H)
        """
        self.count = 0
        self.result = 0
        
        def inorder(node: Optional[TreeNode]):
            if not node or self.count >= k:
                return
            
            # 遍历左子树
            inorder(node.left)
            
            # 访问当前节点
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            
            # 遍历右子树
            inorder(node.right)
        
        inorder(root)
        return self.result


class SolutionIterative:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        迭代解法（使用栈）：
        - 模拟中序遍历过程
        - 找到第k个元素时停止
        时间复杂度：O(H + k)
        空间复杂度：O(H)
        """
        stack = []
        curr = root
        
        while True:
            # 走到最左边
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # 弹出节点
            curr = stack.pop()
            k -= 1
            if k == 0:
                return curr.val
            
            # 转向右子树
            curr = curr.right

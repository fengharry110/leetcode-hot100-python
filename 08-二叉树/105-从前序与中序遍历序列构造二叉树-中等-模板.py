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

提示:
1 <= preorder.length <= 3000
inorder.length == preorder.length
-3000 <= preorder[i], inorder[i] <= 3000
preorder 和 inorder 均 无重复 元素
inorder 均出现在 preorder
preorder 保证为二叉树的前序遍历序列
inorder 保证为二叉树的中序遍历序列
"""

from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        从前序与中序遍历序列构造二叉树
        
        参数:
            preorder: 前序遍历序列
            inorder: 中序遍历序列
            
        返回:
            构造的二叉树根节点
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例1
    print("=" * 50)
    print("测试用例1: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]")
    preorder1 = [3, 9, 20, 15, 7]
    inorder1 = [9, 3, 15, 20, 7]
    root1 = solution.buildTree(preorder1, inorder1)
    print(f"根节点值: {root1.val if root1 else None}")
    print(f"期望根节点值: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: preorder = [-1], inorder = [-1]")
    preorder2 = [-1]
    inorder2 = [-1]
    root2 = solution.buildTree(preorder2, inorder2)
    print(f"根节点值: {root2.val if root2 else None}")
    print(f"期望根节点值: -1")

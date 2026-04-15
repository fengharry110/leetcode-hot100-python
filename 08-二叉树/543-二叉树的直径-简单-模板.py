"""
543. 二叉树的直径
https://leetcode.cn/problems/diameter-of-binary-tree/description/

给你一棵二叉树的根节点 root ，返回该树的 直径 。

二叉树的 直径 是指树中任意两个节点之间最长路径的 长度 。这条路径可能经过也可能不经过根节点 root 。

两节点之间路径的 长度 由它们之间边数表示。

示例 1：
输入：root = [1,2,3,4,5]
输出：3
解释：3 ，取路径 [4,2,1,3] 或 [5,2,1,3] 的长度。

示例 2：
输入：root = [1,2]
输出：1

提示：
树中节点数目在范围 [1, 10^4] 内
-100 <= Node.val <= 100
"""

from typing import Optional


class TreeNode:
    """
    二叉树节点类
    """
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树的直径
        
        参数:
            root: 二叉树根节点
            
        返回:
            二叉树的直径
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1: 完整二叉树
    print("=" * 50)
    print("测试用例1: 完整二叉树 [1,2,3,4,5]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
    solution = Solution()
    diameter1 = solution.diameterOfBinaryTree(root1)
    print(f"直径: {diameter1}")
    print(f"期望结果: 3")
    
    # 测试用例2: 简单二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 简单二叉树 [1,2]")
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    diameter2 = solution.diameterOfBinaryTree(root2)
    print(f"直径: {diameter2}")
    print(f"期望结果: 1")
    
    # 测试用例3: 单节点
    print("\n" + "=" * 50)
    print("测试用例3: 单节点 [1]")
    root3 = TreeNode(1)
    diameter3 = solution.diameterOfBinaryTree(root3)
    print(f"直径: {diameter3}")
    print(f"期望结果: 0")

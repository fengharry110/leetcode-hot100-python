"""
104. 二叉树的最大深度
https://leetcode.cn/problems/maximum-depth-of-binary-tree/description/

给定一个二叉树 root ，返回其最大深度。

二叉树的 最大深度 是指从根节点到最远叶子节点的最长路径上的节点数。

示例 1：
输入：root = [3,9,20,null,null,15,7]
输出：3

示例 2：
输入：root = [1,null,2]
输出：2

提示：
树中节点数目在范围 [0, 10^4] 内
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
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树的最大深度
        
        参数:
            root: 二叉树根节点
            
        返回:
            二叉树的最大深度
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1: 完整二叉树
    print("=" * 50)
    print("测试用例1: 完整二叉树 [3,9,20,null,null,15,7]")
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    solution = Solution()
    depth1 = solution.maxDepth(root1)
    print(f"最大深度: {depth1}")
    print(f"期望结果: 3")
    
    # 测试用例2: 只有右子树的二叉树
    print("\n" + "=" * 50)
    print("测试用例2: 只有右子树 [1,null,2]")
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    depth2 = solution.maxDepth(root2)
    print(f"最大深度: {depth2}")
    print(f"期望结果: 2")
    
    # 测试用例3: 空树
    print("\n" + "=" * 50)
    print("测试用例3: 空树 []")
    root3 = None
    depth3 = solution.maxDepth(root3)
    print(f"最大深度: {depth3}")
    print(f"期望结果: 0")
    
    # 测试用例4: 单节点
    print("\n" + "=" * 50)
    print("测试用例4: 单节点 [1]")
    root4 = TreeNode(1)
    depth4 = solution.maxDepth(root4)
    print(f"最大深度: {depth4}")
    print(f"期望结果: 1")

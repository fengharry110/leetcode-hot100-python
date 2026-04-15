"""
124. 二叉树中的最大路径和
https://leetcode.cn/problems/binary-tree-maximum-path-sum/description/

二叉树中的 路径 被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中 至多出现一次 。该路径 至少包含一个 节点，且不一定经过根节点。

路径和 是路径中各节点值的总和。

给你一个二叉树的根节点 root ，返回其 最大路径和 。

示例 1：
输入：root = [1,2,3]
输出：6
解释：最优路径是 2 -> 1 -> 3 ，路径和为 2 + 1 + 3 = 6

示例 2：
输入：root = [-10,9,20,null,null,15,7]
输出：42
解释：最优路径是 15 -> 20 -> 7 ，路径和为 15 + 20 + 7 = 42

提示：
树中节点数目范围是 [1, 3 * 10^4]
-1000 <= Node.val <= 1000
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
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        计算二叉树中的最大路径和
        
        参数:
            root: 二叉树根节点
            
        返回:
            最大路径和
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1: 简单二叉树
    print("=" * 50)
    print("测试用例1: 简单二叉树 [1,2,3]")
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    solution = Solution()
    result1 = solution.maxPathSum(root1)
    print(f"最大路径和: {result1}")
    print(f"期望结果: 6")
    
    # 测试用例2: 包含负数
    print("\n" + "=" * 50)
    print("测试用例2: 包含负数 [-10,9,20,null,null,15,7]")
    root2 = TreeNode(-10)
    root2.left = TreeNode(9)
    root2.right = TreeNode(20)
    root2.right.left = TreeNode(15)
    root2.right.right = TreeNode(7)
    solution2 = Solution()
    result2 = solution2.maxPathSum(root2)
    print(f"最大路径和: {result2}")
    print(f"期望结果: 42")
    
    # 测试用例3: 单节点
    print("\n" + "=" * 50)
    print("测试用例3: 单节点 [-3]")
    root3 = TreeNode(-3)
    solution3 = Solution()
    result3 = solution3.maxPathSum(root3)
    print(f"最大路径和: {result3}")
    print(f"期望结果: -3")

"""
437. 路径总和 III
https://leetcode.cn/problems/path-sum-iii/description/

给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的 路径 的数目。

路径 不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

示例 1：
输入：root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
输出：3
解释：和等于 8 的路径有:
1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

示例 2：
输入：root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
输出：3

提示:
二叉树的节点个数的范围是 [0,1000]
-10^9 <= Node.val <= 10^9 
-1000 <= targetSum <= 1000 
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        求二叉树里节点值之和等于 targetSum 的路径数目
        
        参数:
            root: 二叉树根节点
            targetSum: 目标和
            
        返回:
            满足条件的路径数目
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    # 测试用例1
    print("=" * 50)
    print("测试用例1: targetSum = 8")
    root1 = TreeNode(10)
    root1.left = TreeNode(5)
    root1.right = TreeNode(-3)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(2)
    root1.right.right = TreeNode(11)
    root1.left.left.left = TreeNode(3)
    root1.left.left.right = TreeNode(-2)
    root1.left.right.right = TreeNode(1)
    solution = Solution()
    result1 = solution.pathSum(root1, 8)
    print(f"结果: {result1}")
    print(f"期望结果: 3")
    
    # 测试用例2
    print("\n" + "=" * 50)
    print("测试用例2: targetSum = 22")
    root2 = TreeNode(5)
    root2.left = TreeNode(4)
    root2.right = TreeNode(8)
    root2.left.left = TreeNode(11)
    root2.right.left = TreeNode(13)
    root2.right.right = TreeNode(4)
    root2.left.left.left = TreeNode(7)
    root2.left.left.right = TreeNode(2)
    root2.right.right.left = TreeNode(5)
    root2.right.right.right = TreeNode(1)
    result2 = solution.pathSum(root2, 22)
    print(f"结果: {result2}")
    print(f"期望结果: 3")

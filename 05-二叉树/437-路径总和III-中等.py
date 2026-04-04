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
"""

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        前缀和 + 哈希表解法：
        - 使用前缀和记录从根节点到当前节点的路径和
        - 如果当前前缀和 - targetSum 存在于哈希表中，说明找到了一条路径
        时间复杂度：O(n)
        空间复杂度：O(h)
        """
        prefix_sum_count = defaultdict(int)
        # 前缀和为0的路径有1条（空路径）
        prefix_sum_count[0] = 1
        
        def dfs(node: Optional[TreeNode], curr_sum: int) -> int:
            if not node:
                return 0
            
            # 更新当前路径和
            curr_sum += node.val
            
            # 以当前节点结尾的路径数
            count = prefix_sum_count[curr_sum - targetSum]
            
            # 更新前缀和计数
            prefix_sum_count[curr_sum] += 1
            
            # 递归遍历左右子树
            count += dfs(node.left, curr_sum)
            count += dfs(node.right, curr_sum)
            
            # 回溯：恢复前缀和计数
            prefix_sum_count[curr_sum] -= 1
            
            return count
        
        return dfs(root, 0)


class SolutionBruteForce:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        暴力解法：
        - 对每个节点，计算以它为起点的所有路径
        时间复杂度：O(n^2)
        空间复杂度：O(h)
        """
        def countPaths(node: Optional[TreeNode], target: int) -> int:
            if not node:
                return 0
            
            count = 0
            if node.val == target:
                count += 1
            
            count += countPaths(node.left, target - node.val)
            count += countPaths(node.right, target - node.val)
            
            return count
        
        if not root:
            return 0
        
        # 以当前节点为起点的路径数
        count = countPaths(root, targetSum)
        
        # 加上左右子树的路径数
        count += self.pathSum(root.left, targetSum)
        count += self.pathSum(root.right, targetSum)
        
        return count

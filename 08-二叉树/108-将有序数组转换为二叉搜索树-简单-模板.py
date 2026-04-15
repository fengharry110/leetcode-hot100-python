"""
108. 将有序数组转换为二叉搜索树
https://leetcode.cn/problems/convert-sorted-array-to-binary-search-tree/description/

给你一个整数数组 nums ，其中元素已经按升序排列，请你将其转换为一棵高度平衡二叉搜索树。
高度平衡二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1」的二叉树。

示例 1：
输入：nums = [-10,-3,0,5,9]
输出：[0,-3,9,-10,null,5]

示例 2：
输入：nums = [1,3]
输出：[3,1]

提示：
1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums 按 严格递增 顺序排列
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    请在此处实现你的解法
    """
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        将有序数组转换为高度平衡二叉搜索树
        
        参数:
            nums: 升序排列的整数数组
            
        返回:
            高度平衡的二叉搜索树根节点
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    print("=" * 50)
    print("测试1: nums = [-10, -3, 0, 5, 9]")
    result1 = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(f"根节点值: {result1.val if result1 else None}")
    print(f"期望根节点值: 0")
    
    # 测试2
    print("\n" + "=" * 50)
    print("测试2: nums = [1, 3]")
    result2 = solution.sortedArrayToBST([1, 3])
    print(f"根节点值: {result2.val if result2 else None}")
    print(f"期望根节点值: 1 或 3")

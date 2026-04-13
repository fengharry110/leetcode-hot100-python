# 108. 将有序数组转换为二叉搜索树
# 给你一个整数数组 nums ，其中元素已经按升序排列，请你将其转换为一棵高度平衡二叉搜索树。
# 高度平衡二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1」的二叉树。
#
# 示例 1：
# 输入：nums = [-10,-3,0,5,9]
# 输出：[0,-3,9,-10,null,5]
#
# 示例 2：
# 输入：nums = [1,3]
# 输出：[3,1]

from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            
            mid = (left + right) // 2
            root = TreeNode(nums[mid])
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root
        
        return build(0, len(nums) - 1)


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    result1 = solution.sortedArrayToBST([-10, -3, 0, 5, 9])
    print(f"测试1根节点: {result1.val}")  # 期望输出: 0
    
    # 测试2
    result2 = solution.sortedArrayToBST([1, 3])
    print(f"测试2根节点: {result2.val}")  # 期望输出: 3 或 1

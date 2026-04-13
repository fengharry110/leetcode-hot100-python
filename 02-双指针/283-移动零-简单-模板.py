"""
283. 移动零
https://leetcode.cn/problems/move-zeroes/description/

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
请注意，必须在不复制数组的情况下原地对数组进行操作。

示例 1:
输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:
输入: nums = [0]
输出: [0]

提示:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

进阶：你能尽量减少完成的操作次数吗？
"""

from typing import List


class Solution:
    """
    请在此处实现你的解法
    """
    
    def moveZeroes(self, nums: List[int]) -> None:
        """
        将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
        
        参数:
            nums: 整数数组
            
        返回:
            None (原地修改数组)
        """
        # TODO: 在此实现你的解法
        pass


if __name__ == "__main__":
    solution = Solution()
    
    # 测试1
    nums1 = [0, 1, 0, 3, 12]
    solution.moveZeroes(nums1)
    print(f"测试1结果: {nums1}")  # 期望输出: [1, 3, 12, 0, 0]
    
    # 测试2
    nums2 = [0]
    solution.moveZeroes(nums2)
    print(f"测试2结果: {nums2}")  # 期望输出: [0]
